
# Good practices following PEP 8# Good practices following PEP 8
# A good python script should not have too much blank space
# should have good and meaningfull names
# 

# Good example of meaningfull name

def calculate_area(radies):
    pass

# Bad example of meaningfull name

def calc(r):
    pass


# Python operators


"""
Name of operator                 symbole with example
Aaddition                         x+y
Substraction                      x-y
Multiplication                    x*y
Division                          x/y
Modulus                           x%y
Exponentiation                    x**y
Floor Division                    x//y
"""

# Comparison operators

"""
Name of operator                 Symbol
Equal                            ==
Greater than                     >
Less then                        <
Less or equal                    <=
Greater or equal                 >=

"""

# Logical operators
"""
Name                             Symbol
And                              and   
Or                               or     
Not                              not

"""

# Membership operators
"""
Name                             Symbol
In                               in                           
Not in                           not in

"""

# Example of bitwise operators

"""
Name                             Symbol
AND                              &                           
OR                               |
XOR                              ^
NOT                              ~
"""

# List and dictionary comprehensions

"""
List comprehension provide a concise way to create lists and dictionaries
Symbols for list and dictionary

List                  [] square brackets  Used to store multiple values in a single variable
Dictionary            {} curly brackets   Used to store data values in form of key/value pairs
"""

# Example  : Basic list comprehension
# Create a list of squares in range of 10

list_of_squares = [x**2 for x in range(10)]
print(list_of_squares)

# Exercise 1:  List of even squares in the range of 20
even_list=[x**2 for x in range(20) if x%2 ==0]
print(even_list)
#Example 2: Dictionary comprehension
# Create a dictionary comprehension for favorite cars and count the lengths of the characters

cars = ['honda', 'mustang', 'toyota', 'benz']

car_lengths = {car: len(car) for car in cars}

print(car_lengths)
#Exercise 2:
#create a list of tuples where each tuple contains a number and its cube for
#for numbers between 1-10
cubes_dict ={x:x**3 for x in range(1,11)}
cubes_list = list(cubes_dict.items())
print(cubes_list)