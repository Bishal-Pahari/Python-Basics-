#varibale is a container to store a value

'''
this is a 
multiline comment or 
docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
Variable Rules:
    - var names are case sensitive
    - must start with letter or underscore
    -can have numbers but cant start with one
"""

x = 1 # int
y = 2.5 # float 
name = 'john' # string
is_true = True # bool

# Multiple assignment
x, y, name, is_cool = (1, 2.5, "john", True)

print("hello")
print(x, y, name, is_cool)

# Check Type
print(type(x))

# Casting 
a = int(x)
b = str(y)
c = float(y)

print (type(c), c)

