# A for loop is used for iterationg over a squence (either a list, a tuple, adictionary, a aset, or a string)

people = ["Gore", "Kale", "Motu", "Patlu"]

# simple for loop 
# for person in people:
#     print(f"curernt person: {person} ")

# break 
# for person in people:
#     print(f"curernt person: {person} ")
#     if person == "Motu":
#         break
    
# Continue {skips Motu and keep continuing}
# for person in people:
#     if person == "Motu":
#         continue
#     print(f"curernt person: {person} ")

# range 
# for i in range(len(people)):
#     print(people[i])
    

# while Lopps execute a set of statements as long as a condition is true 
count = 0
while count <=10:
    print(f"Count: {count}")
    count += 1