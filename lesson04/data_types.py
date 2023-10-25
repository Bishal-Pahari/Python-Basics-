import math

# string data types

# literal assignment
first = "Bishal"
last = "Pahari"


print(type(first))

# constructor function
pizza = str("pepproni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))


# Casting a number into string
year = str(1980)
print(type(year))

print("i Like music from " + year + "s.")

# Multiple lines
multilines = """
Hey, How are you?

I was just checking in.

                        All good?
"""

print(multilines)

# escaping special characters

sentence = 'he said,"i\'m nepali \t who? \n not me" '
print(sentence)


# string methods

sent = "Hello"
print(sent.upper())
print(sent.lower())


print(multilines.title())
print(multilines.strip())
print(len(multilines))
print("")

# build a Menu
title = "menu".upper()
print(title.center(30, "="))
print("coffee".ljust(26, ".") + "$1".rjust(4))


# Some methods return boolean data
print(first.startswith("b"))
print(first.endswith("i"))

# Complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)


# built in functions for numbers
gpa = 3.141592653
print(abs(gpa * -1))
print(round(gpa, 2))

print(math.pi)
print(math.sqrt(gpa))
print(math.floor(gpa))
print(math.ceil(gpa))

# casting string to Number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# error if you attempt to cast incorrect data
zip_value = int("New York")
