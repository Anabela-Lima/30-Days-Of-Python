# Arithmetic Operations in Python
# Integers

from cmath import pi, sqrt
import math
from xml.dom.pulldom import CHARACTERS


print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total) # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False


# My Turn on Exercises 



# Declare your age as integer variable

my_age = 100
# Declare your height as a float variable
my_height =  5.4
# Declare a variable that store a complex number
complex_number =  4 + 7j
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100

base, height = int(input("Enter a base value: ")), int(input("Enter a height value: "))
print("base:", base, "height:",height)

print(type(base))
print(type(height))


area = ((base * height)/2 ) 
print(area)
print("For a given base of", base, "and height of ", height, " The area is ", area, "m^2")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

side_a, side_b, side_c= int(input("Enter length of side a: ")), int(input("Enter length of side b: ")), int(input("Enter length of side c: "))

# print(" The perimeter for your given sides is ", perimeter)
print("a:", side_a, "b:", side_b, "c:", side_c)
print("Perimeter", sum([side_a,side_b,side_c]), "m")


# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length, width, area, perimeter = int(input("Enter length: ")), int(input("Enter width: ")), (length*width), (2 * (length + width))
print("area:", area, "m^2")
print("perimeter: ", perimeter, "m")

import math

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r= int(input("Enter radius: ")) 
area, c= (pi * (r ** 2)), (2 * pi * r)    # note cannot put r, area and c inline because it needs to be used for next parameter

print("r", r)
print("area", area, "m^2")
print("circumference", c, "m" )

# Calculate the slope, x-intercept and y-intercept of y = 2x -2

slope, xintercept, yintercept =  2, (2/2), (-2)

# x intercept is set y= 0 and solve for x
# y intercept is set x = 0 and solve for y

print( "Slope, which is basically ", slope)
print( "x intercept is:", xintercept)
print( "y intercept is:", yintercept )


# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

slope = ((10-2)/(6-2))
print("slope", slope)


# Euclidian distance

a = (2,2)
b = (6,10)

distance = math.sqrt((10 - 2)**2 + (6 - 2)**2)
print("distance", distance)

# Compare the slopes in tasks 8 and 9

# The slopes for both question 8 and 9 are 2 


# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0

a, b, c = 1, 6, 9

x1 = 0.5*(a)*(-b + sqrt((b**2) -(4*a*c)))
x2 = 0.5*(a)*(-b + sqrt((b**2) -(4*a*c)))
print(x1,x2)


# Find the length of 'python' and 'dragon' and make a falsy comparison statement.

# declare variables 
python = "python"
dragon = "dragon"

# have a counter  start at value 0
# loop through the variables- for every letter in variable, increment counter by 1 


def wordLength(str):
    counter = 0 
    for letter in str:
        counter += 1
    print("The length of your word is", counter)

    return counter 

wordLength(dragon)


 # falsy comparison 

# A comparison that yields a false boolean result 


print(wordLength(python) != wordLength(dragon))
print(wordLength(python) > wordLength(dragon))
print(wordLength(python) < wordLength(dragon))
print("Declaring that the two words are equal ",  python is  dragon)
print("two not comparisons",  not not dragon is python ) # Dragon is python => dragon and python are the same = False. Apply first not = not(False  = True, then apply second not =  not(True) = False



# Q13.  Use and operator to check if 'on' is found in both 'python' and 'dragon'

print("on found in both python and dragon:", "on" in "python" and  "on" in "dragon" )



# Q14.  I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

sentence = "I hope this course is not full of jargon"
print("on in sentence:", "on" in sentence)

# Q15. There is no 'on' in both dragon and python

print( "No on in both dragon and python: " ,"on" not in "dragon" and "on" not in "python")

# Q16. Find the length of the text python and convert the value to float and convert it to string 


def lengthFinder(str):
    counter = 0
    for letter in str:
        counter += 1
    print("word length:", counter) 
    return counter


lengthPython = lengthFinder(python)
lengthDragon = lengthFinder(dragon)     

lengthPython_float, lengthPythonString = print("float Python: ", float(lengthPython)), print("String python: ",str(lengthPython))
lengthDragon_float, lengthDragonString = print("float Dragon: ", float(lengthDragon)), print("String Dragon: ",str(lengthDragon))




# Q17.  Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?


def divisibleByTwo(int):
    if int % 2 == 0:
        print(int, "is divisible by two")
    else: print(int, "is not divisible by two")     


divisibleByTwo(3)    


# Q18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

def floorDivisionChecker(int1, int2 ):
    myNumbers= [int1, int2]
    if myNumbers[0] // myNumbers[1] == int(2.7):
        print("YES")
    else: print("Take the L")    


floorDivisionChecker(7,3)

# Q19 Check if type of '10' is equal to type of 10

print(f'type of "{10}"  equal to type of 10 :', type('10') is type(10) )


# Q20 Check if int('9.8') is equal to 10

print(f'int(\'9.8\') is equal to 10')

# Q21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours, ratePerHour= int(input("Enter Hours:" )), int(input("rate per hour: "))
weeklyEarning= (hours*ratePerHour)

print("Hours: ", hours, "Rate per hour: ", ratePerHour, "Weekly Earning: £", weeklyEarning)


'''
Q22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.

'''

numberYears = int(input("Enter number of years:"))

secondsCanLive =  print("A person can live:", numberYears  * 365 * 24 * 60 * 60, "seconds")



'''
Q23.

Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125

'''
# a pattern I can see is that the first number is x^1, second is x^0, x^1, x^2, x^3 
'''
Solution 1 
'''

a = [ 1,2,3,4,5,]


for num in a :          # take 1st number in a , which is 1 
    result =  [num]     # and we store it in an array 
    n = 0               # we have some power n which starts at 0

    while n < 4:                     # for as long as n is less than 4 (we only want to go up to cubic i.e. n= 3)
        result.append(num**n)        # add the new number with power applied to the original result list whic is num
        n +=1                        # n goes up in 1 
    print(*result)                  # print - we dont know how many arguments will be passed into the function so we use * prefix- it also prints it nicer



1
result = [1]
n =0 

n =1 

[1]

n = 2 

[1, 1]

n = 3 

[(1), 1, 1, 1, 1]

# second iteration i =2 -----------

[(2)]

n =0 
2^1

[(2), 1]
n =1 

2^1

[(2), 1, 2]

n = 2 

2^2

[(2), 1, 2, 4 ]

n = 3 

2^3

[(2), 1, 2, 4 , 8]


# 3rd and 4th iterations are the same




'''
Solution 2
'''

# for x in range(6):              # print 5 numbers 
#       if x == 0:
#          continue
     
# print(x, x**0, x**1, x**2, x**3)


for x in range(1,6):
    print(x, x**0, x**1, x**2, x**3)






