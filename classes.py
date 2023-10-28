# A class is like a blueprint for creating objects. An object has properties and method (functions) associated with it. Almost
# everything in python is an object.

# create Class
class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        
    def greeting(self):
        return f"My name is {self.name} and I am {self.age}"
    
    def has_birthday (self):
        self.age += 1
        
# extend class 
class Customer(User):
    # Constructor 
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
        
    def set_balance(self, balance):
        self.balance = balance
        
    def greeting(self):
        return f"My name is {self.name} and I am {self.age}. i have balance of {self.balance}"    

# Init user object
bishal = User("Bishal Pahari", "bishal@test.com", 21)

# init customer object
jasmine = Customer("jasmine Thapa", "jasmine@test.com", 19)

jasmine.set_balance(200)
print(jasmine.greeting())

bishal.has_birthday()
print(bishal.greeting())