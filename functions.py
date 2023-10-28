''' A Function is a block of code which only runs when it is called. In python, we dont use curly brackets, we use 
indentation with tabs or space '''

# create function
def say_hello(name):
    print(f"Hello {name}")
    
say_hello("Bishal")

# return values
def get_sum (num1 = 1, num2 = 2):
    sum = num1 + num2
    return sum

print(get_sum())


# A lambda fn is a small anonymous function
# A lambda fn can take any number of arguments, but can only have one expression. Very similar to JS arrow Function

get_mul = lambda num1, num2 : num1 * num2

print(get_mul(2,3))