# A Modules is basciall a file containing a set of functions to include in your application.
# There are core python modules, modules you can install using the pip package manager (including Django) as 
# well as custom modules

# core modules
import datetime 
from datetime import date
import time

# Pip modules
from camelcase import CamelCase

# Import custom module
from validator import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time.time()

c = CamelCase()
print(c.hump("hello there world"))

email = "test@test.com"

if validate_email(email):
    print("valid email")
else:
    print("Invalid email")

print(f"{today} and {timestamp}")