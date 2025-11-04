import re

def check_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return "OK"
    else:
        return "WRONG"

email = input("")
print(check_email(email).upper())