import re

def main():
    pw = raw_input("Enter your password")
    object = validate(pw)

def validate(pw):
    if len(pw) < 6 or len(pw) > 12:
        print("not valid")
    else:
        if(bool(re.search('[a-z]',pw)) and bool(re.search('[A-Z]',pw)) and bool(re.search('[0-9]',pw)) and bool(re.search('[$#@]',pw))):
            print("valid")
        else:
            print("not valid")
main()
