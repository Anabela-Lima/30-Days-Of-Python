#https://www.w3resource.com/python-exercises/dictionary/

# 1. Write a Python script to sort (ascending and descending) a dictionary by value                                    # Sorting by keys and values (Ascendig + Descending) dictionary


colours = {'red':5, 'pink':4,'yellow':4,'brown':2,'green':3, 'black':1,'blue':2 }

print("colours printed:", colours)

# sorted by key 

print('\n By key:\n')
colours_sorted_key = {k:v for k,v in sorted(colours.items())}
print("colours sorted by key:", colours_sorted_key)

# sorted by value 

print('\n By value ascending:\n')

colours_sorted_value_ascending = {k:v for k,v in sorted(colours.items(), key= lambda v: v[1])}
print("colours by value ascending:", colours_sorted_value_ascending)

print('\n By value Decending:\n')

colours2 = {'red':5, 'pink':4,'yellow':4,'brown':2,'green':3, 'black':1,'blue':2 }
colours_sorted_value_descending = {k:v for k,v in sorted(colours2.items(), key = lambda v:v[1], reverse = True)}
print(colours_sorted_value_descending, type(colours_sorted_value_descending))


print('\n -----------Question 2----------:\n')                                                             # Adding keys to a dictionary

# 2. Write a Python script to add a key to a dictionary. Go to the editor

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print("by declaration:", my_dict)

'''
# or we could do:

my_dict.update({2:30})
print("using update:", my_dict)

'''

print('\n -----------Question 3----------:\n')                                                               # joining dictionaries


# 3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dictionary_final = {}

for d in (dic1,dic2,dic3,):
    print(d)
    dictionary_final.update(d)

print("concatenated dictionary:", dictionary_final)



print('\n -----------Question 4----------:\n')                                                               # check if key exists

# . Write a Python script to check whether a given key already exists in a dictionary.


def keyExist(my_key):
    if my_key in dictionary_final:
        print("key exists")
    else: print("key does not exist")


keyExist(6)       


'''
We could also do:

print(dictionary_final.get(5))     returns the corresponding value for this key 5
print(dictionary_final.get('5'))   returns none because the key string 5 does not exist


'''
 

print('\n -----------Question 5------------:\n')                                                            # iterating over a dictionary using loops


# Write a Python program to iterate over dictionaries using for loops

# printing the keys: 
for key in range(1):
    print("dictionary keys:", dictionary_final.keys())

# printing the values:
for key in range(1):
    print("dictionary values:", dictionary_final.values( ))

# printing the first 3 keys:

for kv in range(1):
    print("first 3 keys:", list(dictionary_final.keys())[:3])

# printing the first 3 values:

for kv in range(1):
    print("first 3 values:", list(dictionary_final.values())[:3])

# printing the first 3 key value pairs:

for kv in range(1):
    print("first kv pairs:", list(dictionary_final.items())[:3])




print('\n -----------Question 6------------:\n')                                                              # square dictionary using for loop from 1 to 5

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


square_dict = {}
for x in range(5):
    square_dict.update({x+1:(x+1)**2})

print("square dictionary:", square_dict)


   

print('\n -----------Question 7 ------------:\n')                                                              # square dictionary using for loop from 1 to 15


# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. Go to the editor
# Sample Dictionary {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

square_dict2 = {}

for x in range(15):
    square_dict2.update({x+1:(x+1)**2})

print("Square dictionary 1 to 15:", square_dict2)


'''
Reformatted solution:

square_dict2 ={}

for x in range(1,16)
square_dict2[x] = x**2

print("Square dictionary 1 to 15:", square_dict2)

'''

print('\n -----------Question 8 ------------:\n')                                                              # square dictionary using for loop from 1 to 15

# 8. Write a Python script to merge two Python dictionaries

def dict_merger(*dic):                     # since we dont know how many arguments will be passed we can do *

    merged_dictionary = {}                 # initialise the empty dictionary
    for d in (dic):                        #for some dictionary refernced 'd' that is passed as argument       
        print(d)                           # print the dictionary passed
        merged_dictionary.update(d)        # update the empty dictionary with the passed dictionary
    print("merged dictionarynew_dict:", merged_dictionary)


# using the function:

dic3 = {2:1, 4:5, 6:8}
dic4 ={9:3, 6:4, 7:1}
dic5 ={12:6, 65:4, 73:7}

dict_merger(dic3,dic4,dic5)


print('\n -----------Question 9 ------------:\n')                                                             # summing items in a dictionary

# Write a Python program to sum all the items in a dictionary.

# dictionary_to_sum = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

def dictionarySum(dic):

    dictionary_values= dic.values()
    print(dictionary_values)
    print("sum of dictionary:", sum(dictionary_values))



# using the function:    
dictionarySum({1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225})



print('\n -----------Question 10 ------------:\n')                                                             # Multiplying items in a dictionary

def dictionaryMulti(dic2):
    multiplication_value = 1
    dictionary_values2 = dic2.values()
    print(dictionary_values2)
    
    for val in dictionary_values2:
        print(val)
        multiplication_value = multiplication_value*val

    print("dictionary values multiplied:", multiplication_value )


dictionaryMulti({1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225})



print('\n -----------Question 12 ------------:\n')                                                             # Removing items in a dictionary

# Write a Python program to remove a key from a dictionary.

def removeKey(dic, my_key):
    print('keys:', dic.keys())
   
    if my_key not in dic.keys():
        print("The key does not exist")
    else:  dic.pop(my_key)

    print("The key",'"',my_key,'"', "has been removed:", dic)    
    print(my_colours)


# Using the function 

my_colours =  {'red':5, 'pink':4,'yellow':4,'brown':2,'green':3, 'black':1,'blue':2 }
removeKey(my_colours,'red')


print('\n -----------Question 13 ------------:\n')                                                             # mapping two lists to a dictionary- keys list key values then mapping 

# Write a Python program to map two lists into a dictionary.


def mapListToDictionary(list1, list2):
    
    mapped_dictionary = dict(zip(list1,list2))
    print("Mapped dictionary:", (mapped_dictionary))

# Using the function


keys = ["a", "b", "c", "d", "e"]
values = [1,2,3,4,5]

mapListToDictionary(keys, values)





print('\n -----------Question 14 ------------:\n')                                                             # Sorting by Keys 

#Write a Python program to sort a given dictionary by key.


alphabet_number_dict= {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} 
print("alphabet number_dic:", alphabet_number_dict)

alphabet_number_dict_by_keys = {k:v for k,v in sorted(alphabet_number_dict.items())}
print("alphabet_number_dict sorted by keys:", alphabet_number_dict_by_keys)



print('\n -----------Question 15 ------------:\n')                                                             # Max and minimum Values  

# Write a Python program to get the maximum and minimum value in a dictionary


def maxAndMin(dic):
   dic_max = max(dic.items())
   print("dictionary maximum value:", dic_max)
    

# using the function
letters_num_Dic= {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} 
maxAndMin(letters_num_Dic)



                                                                                                                                                      
def maxAndMin2(dic):
    dic_sorted_values = {k:v for k,v in sorted(dic.items(), key = lambda v: v[1], reverse = True)}
    print("dictionary maximum value:",list(dic_sorted_values.items())[0])

# using the function
letters_num_Dic2= {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} 
maxAndMin2(letters_num_Dic2)


print('\n -----------Question 15 ------------:\n')                                                             # Max and minimum Values  


class Person:                               # we have Person class
  def __init__(self, fname,age,gender):     # we use def to define a user defined function, every class has a function that coems with it
                                            # that gives us details of how object of this class (the instance) type should be constructed- init initializes the attributes of the class
                                            # the self, is reference to the current instance of the class-it is the reference object of the class
                                            # __init__ takes self; the reference object of the class (the object) and populates it with the attributes e.g. fname
    self.firstname = fname                  # this reference instanc eof the person class, takes the attribure first name which is equal to fname
    self.age= age
    self.gender = gender
 
  def printPersonDetails(self):             # we have another user defined function called printPersonDetails, which takes input argument self i.e the reference instance (object) the person class
    print("firstName:", self.firstname)     # this function prints the firstname of the reference instance
    print("Age:", self.age)
    print("Gender:", self.gender)

class Student(Person):                      # we have a second class called student which inherits the properties of the Person class- so it will inherit the attribute: fname
  pass                                      # pass is just a null operation like a placeholder, its used when code is needed, but nothing needs to happen

x = Student("Ana", 18, "female")             # we have a student object stored in the variable x,and since student inherits the properties of the Person class, it will need the property fname
                                             # we assign it to be Mike
x.printPersonDetails()          


