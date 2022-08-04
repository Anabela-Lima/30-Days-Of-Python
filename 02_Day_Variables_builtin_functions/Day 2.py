# Exercises: Level 1-----------------------------------------------------------------------------------------------

# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# Write a python comment saying 'Day 2: 30 Days of python programming'

# Day 2: 30 Days of python programming 

# Declare a first name variable and assign a value to it

from re import sub
from turtle import circle


first_name = "Ana"
# Declare a last name variable and assign a value to it
last_name =  "Lima"
# Declare a full name variable and assign a value to it
full_name = "Ana Lima"
# Declare a country variable and assign a value to it
country = "Italy"
# Declare a city variable and assign a value to it
city = "Rome"
# Declare an age variable and assign a value to it
age = 100
# Declare a year variable and assign a value to it
year = 2035
# Declare a variable is_married and assign a value to it
is_married= True
# Declare a variable is_true and assign a value to it
is_true = True
# Declare a variable is_light_on and assign a value to it
is_light_on = False
# Declare multiple variable on one line

x= fave_colour, month_year, has_siblings, travelled_countries = "red", 3045, True, 18
print(x)

# Exercises: Level 2
# Check the data type of all your variables using type() built-in function

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))



# Using the len() built-in function, find the length of your first name

print(len(first_name))
# Compare the length of your first name and your last name
len_firstName, len_lastName = print("length of first name is:", 
len(first_name)), print("length of last_name is:" , len(last_name))

# Declare 5 as num_one and 4 as num_two

num_one = 5
num_two = 4
# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)

using_sum = sum([num_one, num_two])
print("computed using sum function:", using_sum)

# Subtract num_two from num_one and assign the value to a variable diff

subtraction= num_two - num_one
print(subtraction)

# Multiply num_two and num_one and assign the value to a variable product

multiplication = num_one * num_two
print(multiplication)

# Divide num_one by num_two and assign the value to a variable division

division = num_one / num_two
print(division)
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder

modulus = num_one % num_two
print(modulus)
# Calculate num_one to the power of num_two and assign the value to a variable exp

power = num_one**num_two
print(power)
# Find floor division of num_one by num_two and assign the value to a variable floor_division

floor_division = num_one // num_two
print(floor_division)

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle

circle_area = 3.14 * (30)**2
print(circle_area, "m^2")

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circumference = 2*3.14 * (30)
print (circumference, 'm')
# Take radius as user input and calculate the area.
radius = int(input("enter a radius value: "))           # had to convert the input to an int from initial string type

print(type(radius))
circle_area2 = 3.14 * (radius)**2
print(circle_area2, 'm^2')

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords


first_name, last_name, country = input("What is your first name: "), input("What is your last name: "), input("Where are you from?: ")

print("Your first name is", first_name , ", your last name is", last_name, "and you are from", country, ".")