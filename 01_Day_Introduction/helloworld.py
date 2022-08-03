# Introduction
# Day 1 - 30DaysOfPython Challenge

from ensurepip import version


print(2 + 3)   # addition(+)
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)

# note 3 modulus 2 is computed as follows:

# 3 / 2 = 1.5
# 1 x 2 = 2  (1 is the quotient i.e the whole part 1 1/2 from step 1, then we multiply by the divisor (2))
# 3 - 2 = 1  (3 from step 1 (i.e the dividend)  from answer of step 2)

print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set - a non ordered list of items
print(type((9.8, 3.14, 2.7)))    # Tuple- ordered collectioned of mixed types

print(type((9.8, "abc", 0 +3j))) # we can see here that we have a mixed data type and type= tuple

# day  1 exercises


#------------Exc1--------------

# Check the python version you are using

# on terminal: python --version 
# answer = Python 3.10.4

# Open the python interactive shell and do the following operations. The operands are 3 and 4.

# addition(+)

print(3+4)
# subtraction(-)
print(3-4)
# multiplication(3*4)
print (3*4)
# modulus(%)
print(3%4)
# division(/)
print((3/4))
# exponential(**)
print(3**4)
# floor division operator//)
print((3//4))

#-------------Exc2--------------

# Write strings on the python interactive shell. The strings are the following:

# Your name
print("Ana")
# Your family name
print("Lima")
# Your country
print("Portugal")
# I am enjoying 30 days of python
print("I am enjoying 30 days of python")

#-------------Exc3--------------

# Check the data types of the following data:
# 10
print(type(10))
# 9.8
print(type(9.8))
# 3.14
print(type(3.14))
# 4 - 4j
print(type(4-4j))
# ['Asabeneh', 'Python', 'Finland']
print(type(['Asabeneh', 'Python', 'Finland']))
# Your name
print(type("Ana"))
# Your family name
print(type("Lima"))
# Your country
print(type("Portugal"))