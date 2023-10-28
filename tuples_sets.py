# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# create tuple
fruits=("apples", "oranges", "grapes")

# using constructor
# fruits2 = tuple("apples", "oranges", "grapes")

# single value needs trailing comma
fruits3 = ("mango")

# Cant change value tuple
# fruits[0] = "pears"

# delete tuple
del fruits3

# get len
print(len(fruits))

# get value
# print(fruits, fruits)


# A Set is a collection which is unordered and unindexed. No duplicate member

# create set
fruits_set = {"apples", "oranges", "grapes"}

# check if in set
print("apples" in fruits_set)

#add to set
fruits_set.add("papaya")

# remove from set 
fruits_set.remove("grapes")

# clear set 
# fruits_set.clear()

# delete 
# del fruits_set

# duplicate member
fruits_set.add("apples")

# get the value
print(fruits_set)


