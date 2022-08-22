'''
Size- how big or how many rows you want in the pattern 

1. can take input from user: n = int(input("Number of rows:"))

2. can pass it in as a function parameter: def pattern(n)

3. can just assign size as a variable n: n = 5

'''

# Putting together nested loops

# printing 7 stars vertically


#----------------------------

# just printing this empty line to create a space between the previous solution and the next

print(" ")
print("\nsolution 1:\n")


#----------------------------

for x in range(7):
    print("*")      

#----------------------------

# just printing this empty line to create a space between the previous solution and the next

print(" ")
print("\nsolution 2: \n")


#----------------------------

'''
output:

*
*
*
*
*
*
*

'''

# by default, each print is done in one lin e
# to print starts all in one line use end keyword 



for x in range(7):
    print("*", end ="hello")  # end tells us what we want in between each iteration 



'''
output:
*hello*hello*hello*hello*hello*hello*hello

'''
print(" ")
print("\nsolution 3:\n")      # had to use \n to print this on new line otherwise would be in line with the *hello code



# so if we want the stars to be printing all after eachother in one line
# just put end= empty string

for x in range(1,6):                    # range(1,6) means: 1,2,3,4,5  (recall it doesnt take in last argument)
    print("*", end = "")


# another solution 

print("\nsolution 4:\n")


for x in range(5):
    print("#", end= "")     # end= "" means print in one line and separate with empty string i.e. no space



#----------------------------

# just printing this empty line to create a space between the previous solution and the next

print(" ")
print("\nsolution 5:\n")


#----------------------------


for x in range(5):                  # for every 1 row and this happens 5 times
    for y in range(5):              # there is 1 column and this happens 5 times
     print("#", end = "love")       # the row will have a #, then I use end= "" 
    print("hello")                  # after every row  print hello
   
#----------------------------

# just printing this empty line to create a space between the previous solution and the next

print(" ")
print("\n solution 5:2 \n")

#----------------------------


for x in range(5):                  # for every 1 row and this happens 5 times
    for y in range(1):              # there is 1 column and this happens 5 times
     print("#", end = "love")       # the row will have a #, then I use end= "" 
    print("hello")                  # after every row  print hello

#----------------------------

# just printing this empty line to create a space between the previous solution and the next

print(" ")
print("\n solution 6: \n")

#----------------------------

# so now that we can see what solution 3 does, lets modify it to print just a simple grid of stars

for y in range(10):                             # 10 rows
    for x in range(10):                         # 10 columns
        print("*", end = " ")                   # each row has 10 stars, end = "" ensure that each star is printed on the same line and separated by an empty string i.e. a space
    print("")                                   # at the end of the iteration (column) print an empty string- which ensures we get 1 row, 2nd row, 3rd rows until 10 instead of being all in one line         




#----------------------------
# just printing this empty line to create a space between the previous solution and the next

print(" ")

print("\nsolution 7:\n")


#----------------------------

for x in range(20):
    for y in range(20):
        print("$", end = " ")
    print("")    