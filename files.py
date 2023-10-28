# python has functions for creating, reading, updating and deleting files


# open a file 
my_file = open("myfile.txt", "w")

# get some info 
print("Name: ", my_file.name)
print("Is Closed: ", my_file.closed)
print("Opening Mode: ", my_file.mode )

# write to file 
my_file.write("I love Python")
my_file.write(" and javascript")
my_file.close()


# append files 
my_file = open("myfile.txt", "a")
my_file.write("I also like Ruby")
my_file.close()

# Read from file 
my_file = open("myfile.txt", "r+")
text = my_file.read(100)
print(text)