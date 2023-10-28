# Example of a custom module to be imported

import re 

def validate_email(email):
    if len(email) > 7:
        pattern = "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\\.[a-zA-Z0-9-]+)*$"
        return bool(re.match(pattern, email))
