# dictionaries are used to store data in key-value pairs
# A dictionary is an unordered collection of items
# each item is a pair consisting of a key and a value.

#Example 1
# CREATE a dictionary for student persuing software engineering
# the keys must be your name, age, technology , course and year 


student_dict ={
    "name": "Yusuf",
    "age": 26,
    "Technology": "AI and ML",
    "course": "BSSE",
    "year": "YEAR 3"
}
print(student_dict["age"]) # accessing values using keys

print(student_dict.get("technology")) # accessing values using get() method
 
 #dictionaries can also be created with the dict() function
 # my_dict = dict(name='yusuf', age= 22)

#ADDING ITEMS using the assignment operator
student_dict['email'] = 'mulindway6@gmail.com'


#  using the update() function         
student_dict.update({"age":22})
#     OR
# student_dict['age'] = 22

print(student_dict)

# Removing ITEMS 
# pop() method, removes the key and returns its value

student_dict.pop('course')
print(student_dict)

# popitem(), removes the last inserted key-value pair
student_dict.popitem()
print(student_dict)

# clear() method, removes all items from the dictionary

 # exercise
 # remove a key-value pair from the dictionary
 
del student_dict['name']
print(student_dict)

# exercise 
# use if to check if key age is dictionary

if 'age' in student_dict:
    print('age is in the dictionary')
else:
    print('age is not in the dictionary')
    
    # exercise
    # use update to change the age value and add a new key whatsapp 
    
student_dict.update({'age':23, 'whatsapp':256})
print(student_dict)
# keys(), values(), items() methods

"""
keys()  returrns a list containing all keys in the dictionary
value() returns a list containing all values in the dictionary
items() returns a list a tuple for each key value pairs 
"""
