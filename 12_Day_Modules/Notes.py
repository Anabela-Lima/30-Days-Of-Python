
'''
Module= a file containing a set of codes
(a single variable, a function or big code base) or a set of functions 
which can be included in an application.

----
* OS (Operating system module) -perform operating system tasks (e.g. mkdir, cwd etc)

* sys module provides functions and variables used to manipulate different parts of the Python runtime environment

Example of sys module


import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. You are reading the Notes for Modules topic at {} '.format(sys.argv[1], sys.argv[2]))


-------------------------------------------------------------------

Input:

12_Day_Modules/Notes.py Ana 16:22

Output:

Welcome Ana. You are reading the Notes for Modules topic at 16:22 

-------------------------------------------------------------------

* useful sys commands:

largest_integer_value_it_takes, environment_path, python_version  = sys.maxsize, sys.path , sys.version

print("\nlarges integer:\n", largest_integer_value_it_takes, "\nenvironment_path:\n",environment_path, "\npythonversion:\n", python_version)



-------------------------------------------------------------------

*Math Module: module containing many mathematical oeprations and constants


check- what functions it has use command dir(math)

import math
dir(math)

--------------------------------------------------------------------
*import functions in line

from math import pi, sqrt, pow, floor

*import multiple functions at once:

from math import *


--------------------------------------------------------------------


*String Module :  The string module contains a number of functions to process standard Python string


import string  as  s


print("\nall letters lower and upper:\n", s.ascii_letters)
print("\nstring digits:\n", s.digits)
print("\n string punctuation\n", s.punctuation)


--------------------------------------------------------------------


Random Module : gives us a random number between 0 and 0.9999.... The random module has lots of functions 

import random
help(random)

from random import randint as a_random_number_between
print(a_random_number_between(1,100))


'''

