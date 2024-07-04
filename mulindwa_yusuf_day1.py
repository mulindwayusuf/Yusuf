#THIS IS SOME SIMPLE PYTHON SYNTAX

# 1. COMMENTS

# Comments are written after a hash tag symbol in python "#", for example:
# this is a comment


# 2. VARIABLES
# assignment
# variables are assigned values using the = operator, eg:
#variable_name = value

#Naming Rules for variables
#Names must start with a letter or an underscore (_).
#Subsequent characters can be letters, numbers, or underscores.
#Names are case-sensitive, so variable, Variable, and VARIABLE are different variables.
#Avoid using Python reserved keywords like if, else, while, etc.

#examples:
# Valid variable names and assignments
age = 25 #integer variable
_name = "Yusuf" #string variable
temperature = 36.6 #float variable
is_student = True #boolean variable

# Variable reassignment
age = 26  # The variable 'age' now holds the value 26

# Variables can also be assigned the result of expressions
difference = age - 5
greeting = "Hello, " + _name
print(difference)
print(greeting)
