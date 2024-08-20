import re

def process_string(s):
    s = re.sub(r'[aeiouAEIOU]', '', s)
    s = re.sub(r'[^bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ].', '.\\1', s)
    s = s.lower()  
    return s

s = input("")
print(process_string(s))