# Declare a function add_two_numbers. It takes two parameters and it returns a sum.


import math
from operator import indexOf
from os import remove


def mySum(num1,num2):
    
    adding = num1 +num2
    print("sum of", num1, "and", num2, "is:", adding)


mySum(3,4)

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def areaCircle(r, pi = math.pi ):
    area = "{:.2f}".format(pi *(r**2))
    print("area is:" ,area, "m2")

areaCircle(3)

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    total= 0
    for num in nums:
        if type(num) != int:
            print(num ,"is not an integer!")
        else: total += num
    
        
    print("sum of number is:", total )


add_all_nums(3,4,5,6,7)

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def CtoF(c):
    f= (c*(9/5))+32
    print(c, "Celcius is", f, "degrees farenheit")

# using the function

CtoF(32)

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def seasonChecker(month):
    month = month.lower()
    if month == "december" or month== "january" or month== "februay":
        print("it is winter")
    elif month== "march" or month == "april" or month == "may":
        print("it is spring")
    elif month =="june" or month =="july"  or month =="august":
        print("it is summer")
    elif month =="september" or month =="october"  or month =="november":
        print("it is Autum")    
    else: print("I do not recognise that month ")


# using the function:

seasonChecker("July")                                             
    
# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1,y1, x2,y2):
    slope = (x2-x1)/(y2-y1)
    print("The slope is:", slope)


calculate_slope(2, 3, 6, 7)

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def quad(a,b,c):
    
    x1= (-b + math.sqrt((b**2) - (4*a*c)))/(2*a)
    x2= (-b - math.sqrt((b**2) - (4*a*c)))/(2*a)

    print("Root 1 is:", x1, "and root 2 is:", x2)

quad(2,-5,-3)

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(lst):
    print("list:", lst)

print_list([3,4,6,7,2,2])

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(my_array):
    length_array = len(my_array)
    print("length_array", length_array)
        
    new_array= []
    for elements in my_array:
        length_array -=1
        new_array.append(my_array[length_array])

    print("reversed array:", new_array)      

reverse_list([3,4,6,7,2,2])   
reverse_list(["A", "B", "C"])      

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(my_lst):

    cap_list = []
    for element in my_lst:
        cap_list.append(element.upper())
    print("capitalized list:", cap_list)      


capitalize_list_items(["yoghurt", "coffee", "toast", "honey", "sugar", "jam"])    

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(*add):
    my_shopping = ["pancakes", "syrup", "strawberries"]
    my_shopping.extend(*add)
    print("add item list:", my_shopping,)


# using the function:

add_item(["cinnamon", "blueberries"])



## a second function 

def add_item2(the_lst, item ):

    the_lst = the_lst
    the_lst.append(item)
    print("new list:", the_lst)

# using the function:

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
add_item2(food_stuff, "broccoli")    # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];


# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(a_lst, remove_item):

    input_lst_lowered = []

    for item in a_lst:
        input_lst_lowered.append(item.lower())
    
    print("lowered list:", input_lst_lowered)    
    

    remove_item = str(remove_item).lower()
    print("item and item type to be removed:", remove_item, type(remove_item))

    input_lst_lowered.remove(remove_item)
  
    print("list after item removed:", input_lst_lowered)



remove_item(['Potato', 'Tomato', 'Mango', 'Milk', 'Bread', 'Olives'], 'Olives')



# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(_range):

    my_sum_numbers= 0
    the_numbers = []

    for number in range(1,(_range+1)):
        the_numbers.append(number)
        
    print("sum of numebers:", sum(the_numbers) )   


sum_of_numbers(5) # 15
sum_of_numbers(10) # 15
sum_of_numbers(100) # 15

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(my_range2):
    
    odd_els = []
    for el in range(1, (my_range2 +1) ):
        if el %  2 is not 0:
           odd_els.append(el)
    odd_sum = sum(odd_els) 
    print("odd elements:", odd_els)     
    print("elements:",odd_sum)


sum_of_odds(10)


# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even (the_range):

    evens =[]

    for el in range(1, (the_range+1)):
     if el % 2  == 0:
        evens.append(el)
    sum_evens = sum(evens)     
    print("evens:", evens) 
    print("sum of evens:", sum_evens)

sum_of_even(10)

# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.

def evens_and_odds(pos):
    evens_array =[]
    odds_array = []

    even_count = 0 
    odd_count = 0
    
    for el in range(1, (pos+1)):
        if el % 2 == 0:
            print(el, "is even")
            evens_array.append(el)
            even_count +=1
        else: 
            print(el, "is odd")
            odds_array.append(el)
            odd_count +=1
        
          
    print("odds:", odds_array, "evens:", evens_array)
    print("Odd count:", odd_count, "even count:", even_count)           

evens_and_odds(12)
            

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(number):
    n =number
    print("n:", n)
    current_result = number

    for x in range(1,(number)):                #1,6
     
     current_result = current_result * (n-1)
     print("current result:", current_result)
     n -=1
   
    
    print("range:",range(1,(number)))
    print("factorial of", number , "is:", current_result)    
   

factorial(10)
    

# Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(param):
    
    if len(param) == 0:
     print("param is empty")
    else: print ("param is not empty")

is_empty([])


# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# Exercises: Level 3

# Write a function called is_prime, which checks if a number is prime.


# a prime number is a number that is only divisible by itself and 1 
# so non prime number would be a number that is divisible by any in the range of 2- n 


def is_prime(n):
  for i in range(2,n):      # for numbers in the range 2 - say 10 = 2-9
    if (n%i) == 0:          # if the given number is divisible by the any in the range (except itself- since range does not include last number i.e. n)
      print(False)
  print(True)
    
is_prime(10)


# My own question: Write a functions which checks if all items are unique in the list.

def uniqueList(a_lst):

    unique_lst = []

    print("original list:", a_lst)
    
    for item in a_lst:
        if not item in unique_lst:
            print("item added:", item)
            unique_lst.append(item)

    print(unique_lst)        



uniqueList(["a","b","c","d","d","a"])


# Write a functions which checks if all items are unique in the list.

# have a unique_item_counter = 0
# increment unique_item_counter by 1
# if unique_item_counter = to length of user list => print list is unique return true


print("")

def _isListUnique(user_list):

    i = 0
    unique_counter = 0
    for item in range(len(user_list)):
      print("\n i=", i, "- " "user list before removing: \n", user_list)
      remove_item = user_list[i]
      print("item at index:", i, "=" , remove_item)
      print("item to be removed:", remove_item)
      user_list.pop(i)
      print("user list after removing", user_list)
      item_in_list = remove_item in user_list
      print("item:",remove_item, "in list? : ", item_in_list)

      if not item_in_list:
        unique_counter +=1
        print("unique")

         


    
      

      

  
        


_isListUnique([1,2,3,1,4,5])







# def checkItem (a_lst):

#     an_array = []

#     for itm in a_lst:
#         print("array before:", an_array)
#         if itm in an_array: 
#             print("List is not unique", itm, "is in there already!")
                
#         else: an_array.append(itm) 
#         print("the item added", itm)
    

#     i = an_array[y]
#     y = 0

#     for my_item in an_array:
#         y += 0
#         print(my_item)
     
#         # if my_item != i:
#         #     print("list is unique ") 
        

      
           
           
            
            

   
    # print(an_array)
                

# checkItem(["a","b","c","d"])

# Write a function which checks if all the items of the list are of the same data type.
# Write a function which check if provided variable is a valid python variable
# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.



