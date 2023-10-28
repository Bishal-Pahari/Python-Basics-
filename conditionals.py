# if/else condition are used to decide to do smthng being true or false

x = 3
y = 5


# Condition operators( ==, !=, >, <, >=, <=) - used to compare values
# if x < y : 
#     print(f"{x} is smaller than {y}")
# elif y < x:
#     print(f"{y} is smaller than {x}")
# else:
#     print(f"{x} is equal to {y}")
    
# nested if 
# if x>2:
#     if x<10:
#         print(f"{x} is greater than 2 and less than or equal to 10")

# logical operators( and, or , not) - used to combine conditional statements

# and
# if x>2 and x <= 10: 
#     print(f"{x} is greater than 2 and less than or equal to 10")

# # or
# if x>2 or x <= 10: 
#     print(f"{x} is greater than 2 and less than or equal to 10")

# # not 
# if not(x==y):
#     print(f"{x} is not equal to {y}")


# membership operators (not, not in) - membership operators are used to test if a squence is presented in an object

numbers = [1,2,3,4,5]

# in 
if x in numbers:
    print(x in numbers)

# not in 
if x not in numbers:
    print(x in numbers)
    
# is 
if x is y:
    print(x is y)

# is not
if x is not y:
    print(x is not y)