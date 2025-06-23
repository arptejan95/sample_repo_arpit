import requests
import json
import pandas as pd
import boto3
from io import BytesIO
import configparser
import logging
from datetime import datetime

# === Logging Setup ===
log_file_path = "hrms_api_employee_master_log.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path, mode='w'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# === Load Config ===
config = configparser.ConfigParser()
config.read("params.config")

token_url = config['TOKEN_CONFIG']['TOKEN_URL']
token_payload = config['TOKEN_CONFIG']['TOKEN_PAYLOAD']
token_auth = config['TOKEN_CONFIG']['TOKEN_AUTH']

api_url = config['API_CONFIG']['API_URL']
api_key = config['API_CONFIG']['API_KEY']
api_payload = config['API_CONFIG']['API_PAYLOAD']

s3_secret_key = config['S3_CONFIG']['SECRET_KEY']
s3_access_key = config['S3_CONFIG']['ACCESS_KEY']
s3_bucket_name = config['S3_CONFIG']['BUCKET_NAME']
s3_bucket_path = config['S3_CONFIG']['BUCKET_PATH']
log_path = config['S3_CONFIG']['LOG_PATH']

# Initialize S3 client with AWS access and secret keys
def get_s3_client(s3_access_key, s3_secret_key):
    """Return an S3 client using boto3 with explicit AWS credentials."""
    s3_client = boto3.client(
        's3',
        aws_access_key_id=s3_access_key,
        aws_secret_access_key=s3_secret_key,
        verify=False
    )
    return s3_client

# === Save DataFrame to S3 in Parquet Format ===
def save_to_s3_parquet(df, s3_bucket_name, s3_bucket_path, s3_client):
    """Save the DataFrame to S3 in Parquet format with current date as suffix."""
    current_date = datetime.now().strftime('%Y-%m-%d')
    s3_folder_path = f"{s3_bucket_path}"
    s3_file_name = f"HRMS_Employee_Master_API_{current_date}.parquet"
    s3_key = s3_folder_path + s3_file_name

    # Convert the DataFrame to Parquet and save to S3
    with BytesIO() as buffer:
        df.to_parquet(buffer, engine='pyarrow', index=False)
        buffer.seek(0)
        s3_client.put_object(Bucket=s3_bucket_name, Key=s3_key, Body=buffer)

    logger.info(f"Data saved to S3 at {s3_key}")

# === Upload Log File to S3 ===
def upload_log_to_s3(log_file_path, s3_bucket_name, log_s3_key, s3_client):
    try:
        with open(log_file_path, "rb") as log_file:
            s3_client.put_object(Bucket=s3_bucket_name, Key=log_s3_key, Body=log_file)
        logger.info(f"Log file uploaded to S3 at '{log_s3_key}'")
    except Exception as e:
        logger.error(f"Failed to upload log file to S3: {e}")

def get_new_access_token(token_url, token_payload, token_auth):
    """Refresh the access token using the refresh token."""
    #global ACCESS_TOKEN
    token_headers = {'Authorization': f'Basic {token_auth}',
                     'Content-Type': 'application/x-www-form-urlencoded'
                     }
    
    token_response = requests.request("POST", token_url, headers=token_headers, data=token_payload)

    if token_response.status_code == 200:
        new_token = token_response.json().get("access_token")
        if new_token:
            ACCESS_TOKEN = new_token
            logger.info("Token refreshed successfully!")
        else:
            logger.warning("Failed to retrieve new access token.")
    else:
        logger.error(f"Failed to refresh token: {token_response.status_code}, {token_response.text}")
        ACCESS_TOKEN = None

    return ACCESS_TOKEN


def make_api_request(api_url, api_payload, api_key, token_url, token_payload, token_auth, s3_client, s3_bucket_name, s3_bucket_path, current_timestamp):
    """Make the API request with error handling and accumulate all data."""
    
    ACCESS_TOKEN = get_new_access_token(token_url, token_payload, token_auth)
    if not ACCESS_TOKEN:
        logger.error("Access token could not be retrieved. Exiting API call.")
        return
    
    overall_df = pd.DataFrame()  # Initialize an empty dataframe to store all results

    while True:
        # Prepare headers
        api_headers = {
            "apikey": api_key,
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }

        # Make the API request
        api_response = requests.request("POST", api_url, headers=api_headers, data=api_payload)

        if api_response.status_code == 401:  # Token expired
            logger.warning("Token expired, refreshing...")
            ACCESS_TOKEN = get_new_access_token(token_url, token_payload, token_auth)  # Call your function to refresh the token
            if not ACCESS_TOKEN:
                logger.error("Failed to refresh access token after expiration. Exiting.")
                break
            # Retry the request with new token
            api_headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"
            api_response = requests.request("POST", api_url, headers=api_headers, data=api_payload)

        if api_response.status_code in [200, 201]:
            logger.info("Request Successful!")
        else:
            logger.error(f"Error {api_response.status_code}: {api_response.text}")
            break  # Exit loop if request fails

        # Extract the data from the response body
        try:
            api_response_body = api_response.json()['root']['EmployeeMaster']['EmployeeMasterData']
        except KeyError as e:
            logger.error(f"Invalid response structure: {e}")
            break
        
        rowData_list = []

        for rowCount in range(len(api_response_body)):
            rowData = api_response_body[rowCount]['BasicDetails']['BasicDetail']
            rowData_list.append(rowData)

        df = pd.DataFrame(rowData_list)
        is_load_complete = api_response.json().get('isLoadComplete', False)
        df['isLoadCompleted'] = is_load_complete

        # Add "EXTRACT_TIMESTAMP" column with the current timestamp
        df['EXTRACT_TIMESTAMP'] = current_timestamp

        # Check if 'isLoadComplete' is True and df is empty
        if is_load_complete and df.shape[0] == 0:
            logger.info("Data load complete and no more data available, exiting loop.")
            break

        # If data is returned, concatenate it to overall_df
        if df.shape[0] > 0:
            overall_df = pd.concat([overall_df, df], ignore_index=True)
        else:
            logger.warning("No data returned in this response.")

    # Save the overall DataFrame to S3 as Parquet
    if not overall_df.empty:
        logger.info(f"API returned {len(overall_df)} records.")
        save_to_s3_parquet(overall_df, s3_bucket_name, s3_bucket_path, s3_client)
    else:
        logger.warning("No data to save to S3.")

    logger.info("Data extraction and saving to S3 completed successfully.")
    return

# === Run Script ===
if __name__ == "__main__":
    current_timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000Z')
    parsed_timestamp = datetime.strptime(current_timestamp, '%Y-%m-%dT%H:%M:%S.000Z').strftime('%Y%m%d_%H%M%S')
    logger.info(f"HRMS API data extraction started at {current_timestamp}")

    # Get the S3 client
    s3_client = get_s3_client(s3_access_key, s3_secret_key)

    # API call
    make_api_request(api_url, api_payload, api_key, token_url, token_payload, token_auth, s3_client, s3_bucket_name, s3_bucket_path, current_timestamp)
    logger.info("Data extraction is over")

    # Upload logs to S3
    log_s3_key = f"{log_path}HRMS_Employee_Master_API_{parsed_timestamp}.log"
    upload_log_to_s3(log_file_path, s3_bucket_name, log_s3_key, s3_client)