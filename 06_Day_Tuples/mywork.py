# Exercises: Level 1

# Create an empty tuple

from queue import Empty
from random import random


Books = ()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

sisters= ("Aleyna", "Liona", "Diana", "Belissa", "Ayanna")

print("sisters:", sisters)
brothers = ("Steven", "Mark", "Paul", "Fin", "Chad", "Pedro")
print( "brothers:", brothers)
# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print("Siblings joined:", siblings)
# How many siblings do you have?

print("Number of siblings:", len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

parents = ("dad", "mum")
family_members = parents + siblings
print("family:", family_members)

# Exercises: Level 2

# Unpack siblings and parents from family_members

family_members = list(family_members)
print("list of family members:",family_members)

parent1, parent2, *siblings_list = ['dad', 'mum', 'Aleyna', 'Liona', 'Diana', 'Belissa', 'Ayanna', 'Steven', 'Mark', 'Paul', 'Fin', 'Chad', 'Pedro']

parents_from_list = [parent1, parent2]
print(parents_from_list)

siblings_from_list = siblings_list
print("siblings from list", siblings_from_list)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ("strawberries", "mangoes", "pineapples", "oranges", "grapes","jack fruit")
vegetables = ("carrots", "onions", "spinach", "tomatoes", "peppers", "mushrooms")
animal = ("pig", "cat", "rabbit", "rat", "elephant", "flamingo") 

food_stuff = vegetables + animal + fruits 

print("food_stuff tutple:", food_stuff ) 


# Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff)
print("food_stuff list:",food_stuff_lt) 

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

print("length of food_stuff list:", len(food_stuff_lt))

middle_item = int((len(food_stuff_lt)-1) /2)
print("middle item in list:", middle_item)

print("before slicing out middle item:", food_stuff_lt)
print("after slicing out middle item:", "item removed:", food_stuff_lt.pop(middle_item), "," ,"updated list:", food_stuff_lt , "length of list now:", len(food_stuff_lt))
# now let me try with the tuple- note: we cannot remove items in a tuple like we did above, we saw
# that when we popped middle item, length of list reduced by 1. However, tuples cannot be modified, food_stuff[middle_item] will return the middle item
# but not remove it

print("slicing middle item in tuple", food_stuff[middle_item], len(food_stuff))
print("slicing middle item in tuple, then the second after that ", food_stuff[middle_item::2])
print("slicing middle item in tuple, then the second before that going <- way ", food_stuff[middle_item::-2])


# Slice out the first three items and the last three items from food_staff_lt list

print("slice out first 3 and last 3 items:", food_stuff_lt[0:3], food_stuff_lt[14:])    # index 0 to 3 and index 14 until then end = index 17 (since length is 18 => last index =17) 

# For practise I will clear the list and check if it is empty using if else statement 
food_stuff_lt.clear()
if len(food_stuff_lt) == 0:
    print("the list is empty")
else: print("the list is not empty")    

# now lets delete it completely - note the above step is not necessary to delete a list 


del food_stuff_lt
# print(food_stuff_lt)

# NameError: name 'food' is not defined, as expected since we deleted the list 




# Check if an item exists in tuple:

print("aubergine" in food_stuff)

# Check if 'Estonia' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)


# Check if 'Iceland' is a nordic country

print("Iceland" in nordic_countries)