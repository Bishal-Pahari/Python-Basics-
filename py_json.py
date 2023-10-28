# JSON is commonly used with data APIs. Here how we can parse JSON into a python dictionary

import json 

# Sample JSON 
userJSON = '{"first_name":"Bishal", "last_name":"Pahari", "age":30}'

# parse to dict 
user = json.loads(userJSON)

print(user) 
print(user["first_name"])

car = {"make" : "ford", "model": "Mustang", "Year" : 1970}

carJSON  = json.dumps(car)
print(carJSON)
