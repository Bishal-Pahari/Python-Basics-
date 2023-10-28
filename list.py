# A list is a collection which is ordered and changeable. ALlows duplicate members
# basically like arrays in JS

# create list
numbers = [1,2,3,4,5]
fruits=["apple", "oranges", "mango", "guava"]

# using constructor
# numbers2= list((1,2,3,4,5))

# get values
print(fruits[1])

# get length of list 
print(len(fruits))

# append list
fruits.append("strawberry")

# remove from list
fruits.remove("apple")

# insert into position
fruits.insert(2,"berry")

# remove with pop 
fruits.pop(2)

# reverse list
fruits.reverse()

# reverse sort
fruits.sort(reverse=True)

# change value
fruits[0] = "blue cherry"

print(fruits)
