# strings in python are surrounded by either single or Double quotation marks. Let's look at string formatting and some string methods

name = "Bishal"
age = 22

#concatenate
# print("hello my name is " + name + ". I am " + str(age) + " Years old")

# string formatting

# arguments by position
# print('my name is {name} and I am {age}'.format(name = name, age = age))

# F-strings (available in python 3.6+) (similar to string literals in JS)
# print(f"hello my name is {name} and I am {age}")

# string methods
# Capitalize string
s= "Hello world"
print(s.capitalize())

# make all upper case
print(s.upper())

# make all lower case
print(s.upper())

# swap case
print(s.swapcase())

# get len
print(len(s))

# replace
print(s.replace("world", "everyone"))

# count substring
sub = 'h'
print(s.count(sub))

# starts with (returns true or false)
print(s.startswith("Namaste"))

# ends with (returns true or false)
print(s.endswith("nepal"))

# find position
print(s.find('r'))

# split into a list
print(s.split())

# is all alphanumeric
print(s.isalnum())

# is all alphabetic
print(s.isalpha())

# is all numeric
print(s.isnumeric())