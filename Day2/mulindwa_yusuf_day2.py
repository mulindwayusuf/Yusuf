#control structures
# conditional statements

# age = 22

# if age > 18:
#     print ('You are an adult')
    
# elif age > 65:
#     print('You are a senior citizen')
    
# else:
#     print ('You are a youth')
    
    
    
#Grading

# grade = 89

# if grade >=90:
#     print('Excellent')
# elif grade >=80:
#     print('Very good')
# elif grade >=70:
#     print('Good')  
# else:
#     print('Not good')     


    #  exercise (pricing)
# price = 2000    
# age = int(input('Enter your age'))
# if age < 13:
#     print(' You have a discount of shs 1000, Price is:')
#     print( 'shs'+(price-1000))
# elif 13<= age <= 18:
#     print('You have a discount of shs 500 ,Price is:')
#     print( 'shs'+str(price-500))
# elif 18<= age <= 65:
#     print('You are an adult,Price is:')
#     print( 'shs'+str(price))  
# else:
#     print('You are a senior citizen,Price is:')
#     print( 'shs'+str(5000))   
    
   
   
    #LOOPS(for and while loops)   
    
    #Example 3
    
# cars = ['honda', 'mustang', 'toyota', 'benz']

# for car in cars:
#     print( car)

# count = 1
# while count <= 10:
#     print( 'count 1 to 10: ', count)
#     count += 1

# colors = ['blue', 'green', 'red', 'yellow']
# for color in colors:
#     print( color)
    
nums = [1,2,3,4,5]
    
rev_num =[]
i = len(nums)-1

while i >= 0:
    rev_num.append(nums[i])
    i -= 1
    print(rev_num)
    
      
    
    