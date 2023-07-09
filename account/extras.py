import re

def is_email(str):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, str):
        return True
    else:
        return False


