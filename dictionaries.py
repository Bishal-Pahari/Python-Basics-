# similar to object literal(JSON) in JS, hash in Ruby

# create dictionary
person = {
    "first_name" : "Bishal",
    "last_name" : "pahari",
    "age" : 22
}

# print(person, type(person))

people = {
    "person1" : {
        "name" : "ram karan",
        "age" : 32,
    },
    "person2" : {
        "name" : "kiran khamba",
        "age" : 33,
    }
}

# print(people["person1"]["name"], type(people))


# using constructor
# person2 = dict(first_name = "sarah", last_name="williams")
# print(person2, type(person2))



# add key/value
person["phone"] = "983928781";

# get dict keys
print(person.keys())

# get dict items
print(person.items())

# copy dict
person2 = person.copy()
person2["phone"] = "221231232132"
# print("person two details:", person2)

# remove item
del(person["age"])
person.pop("phone")
print("person two details:", person2)

# clear
# person.clear()

# get length
print(len(person))

# list of dictionary
people2 = [
    {"name" : "hari bansha", "age" : 21},
    {"name" : "karan karki", "age": 23}
]

print(people2[1])