# Defining functions

#Function syntax and parameters
#Return values
#Lambda functions


# functions in python are defined using the def keyword
# followed by function name and the parentheses()
# inside the parentheses you put the parameters and then the colon

# Example 1:

def multipy(x, y):
    return x * y
result = multipy(5,10)
print(result)
# print(multipy(5,10))


# exercise 1  

def greet(name = "Yusuf"):
    print("i am software programmer, " + name)
greet()

def get_yus():
    name = "Yusuf"
    age = 37
    return name, age
name,age = get_yus()
print(name, age)

# Notes
# def: keyword to define a function that
# function name: name of the function
# parameters: arguments passed to the function
# Docstrings: optional documentation, describes the function purpose
# return:optional, returns the value from the function

# lambda function
# they are small anonymous functions defined using the lambda keyword.
# they are restricted to a single expression

# syntax
# lambda parameter: expression

# example

add = lambda a, b: a + b

print(add(5,10))

# example: use cases of lambda function for sorting

coordinates = [(1,2), (2,3), (3,1), (5,0)]
coordinates.sort(key = lambda x: x[1])
print(coordinates)

# Map, filter and reduce

number_squares = [1,2,3,4,5]

square = list(map(lambda x: x**2, number_squares))
print(square)

# Exercise : Define a function to get user onfo that accepts
# arbitrary keyword arguments and prints 
# each key-value pair
def get_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

get_user_info(name="Yusuf", age=22, city="Kampala", occupation="Engineer")


     
     

