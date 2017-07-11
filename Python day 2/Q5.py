import re
pw = raw_input("Enter your password")
if len(pw) < 6 or len(pw) > 16:
    print("not valid")
else:
    if(bool(re.search('[a-z]',pw)) and bool(re.search('[A-Z]',pw)) and bool(re.search('[0-9]',pw)) and bool(re.search('[$#@]',pw))):
        print("valid")
    else:
        print("not valid")
