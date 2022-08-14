# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.


string1 = ['Thirty', 'Days', 'Of', 'Python']

print(" ".join(string1))  # " " means join with a gap, you can place anything in there as the separator


# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

string2 = [ 'Coding', 'For' , 'All' ]
print(" ".join(string2))

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4.Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())
# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

swapcase =  print(company.swapcase())  # will convert all lower case to upper case and all uppercase letters to lower case
title = print(company.title())  # will capitalise all initials

# 9. Cut(slice) out the first word of Coding For All string.

sliced = print(company[6:])   # start at index 6 and print what follows 

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("contains word coding at index:",  company.index("Coding"))

# 11. Replace the word coding in the string 'Coding For All' to Python.
print("replace:", company.replace("Coding", "Python"))

# 12. Change Python for Everyone to Python for All using the replace method or other methods.

python_for_everyone = "Python for Everyone"

print(python_for_everyone.replace("Everyone", "All"))

# 13. Split the string 'Coding For All' using space as the separator (split()) .

split = print(company.split(" "))

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

string3 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

split_comma = print(string3.split(","))

# 15. What is the character at index 0 in the string Coding For All.

char_at_index0 = print(company[0])

# 16. What is the last index of the string Coding For All.
length_company = len(company)

datatype_length_company= print(type(length_company))

last_index = length_company -1
print(last_index)


# 17. What character is at index 10 in "Coding For All" string.

company_index_10 = company[10]

if company_index_10 == " " : 
    print("index 10 is just a space ")
    print("result:", company_index_10)
else: print("index 10 is not a space, it is: ", company_index_10)   


# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.-------------------------Attention 

phrase = "Python For Everyone"
# break up the phrase 

broken_phrase = (phrase.split(" "))
print("broken phrase", broken_phrase)

for x in broken_phrase:
     acronym_array = []
     acronym_array.append(x[0])
     a= "".join(acronym_array).upper()
     print(str(a))

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.

phrase2 = "Coding For all"
broken_phrase_2 = (phrase2.split(" "))
print( "broken phrase 2", broken_phrase)

for x in broken_phrase_2:
    acronym_array2 = []
    acronym_array2.append(x[0])
    b = "".join(acronym_array2).upper()
    print(b)
 
# 20. Use index to determine the position of the first occurrence of C in Coding For All.

print("first occurrence of C:", phrase2.index("C"))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print("first occurrence of F ",phrase2.index("F"))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("position of the last occurrence of l:",phrase2.rfind("l"))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

because_phrase = 'You cannot end a sentence with because because because is a conjunction'

print("position of the first occurrence of the word 'because'", because_phrase.index("because") )

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print("position of the last occurrence of the word 'because'", because_phrase.rindex("because") )

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# solution1

first_substring = because_phrase[:31]
second_substring = because_phrase[55:]

string = [first_substring, second_substring]
print("".join(string))

# solution 1 reformatted - version 1

first_substring = because_phrase[:31]
second_substring = because_phrase[55:]
print(first_substring + second_substring)


# solution 2

print(because_phrase[:31] + because_phrase[55:])   # print everying before idex 31 and everything after index 55 of because_phrase variable. Note, use + to concatenate otherwise if you use a , it will add an additional space


# 26. Does 'Coding For All' start with a substring Coding?

print("Start with substring coding", company.startswith("Coding"))


# 27. Does 'Coding For All' end with a substring coding?

print("End with substring coding ", company.endswith("coding"))
# 28. '   Coding For All      '  , remove the left and right trailing spaces in the given string.

string_to_be_stripped = '   Coding For All      ' 
print(string_to_be_stripped.strip(' '))

# 29. Which one of the following variables return True when we use the method isidentifier():
#  30DaysOfPython
#  thirty_days_of_python  -- This one because it is a valid variable name - the other one starts with a number which is not valid 

# 30. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']


print("# ".join(python_libraries))


# 33. Use the new line escape sequence to separate the following sentences.
#  I am enjoying this challenge.
#  I just wonder what is next.


sentence_no_break = "I am enjoying this challenge. I just wonder what is next"
print(sentence_no_break)

'''
#output:

I am enjoying this challenge. I just wonder what is next

'''

sentence_with_break = "I am enjoying this challenge\nI just wonder what is next"
print(sentence_with_break)

'''
output:

I am enjoying this challenge
I just wonder what is next

'''


# 34. Use a tab escape sequence to write the following lines.
#  Name      Age     Country   City
#  Asabeneh  250     Finland   Helsinki


tab_sentence = "Name\tAge\tCountry\tCity\nAna\t150\tCuba\tHavana"               # the \t adds a default 8 spacing and \n adds a new line like a break
print(tab_sentence)


# 35. Use the string formatting method to display the following:
#   radius = 10
#   area = 3.14 * radius ** 2

# old string formatting method 

'''
format for old style 

variable = ' xyz %s' %()   ---- for string substitution

variable = ' xyz %d' %()   ---- for integer substitution

variable = ' xyz %f' %()   ---- for float point numbers substitution

variable = ' xyz "%' %()   ---- to specify number of decimal places

'''

formatted_string = 'radius = %s' %(10)
print(formatted_string)
print(type(formatted_string))




pi = 3.14    # this is a floating point number 
radius = 5
area = 2 * pi *radius **2
area = 'The area of a circle with radius %.2f is equal to %d '%(radius, area)           # we could do %f but it will print the full floating number i.e. 5.0000 so we restrict it to 2 decimal places by doing %.2f

print(area)



# 36. The area of a circle with radius 10 is 314 meters square.

radius2 = 10 
meters = 314 

area2 = ' The area of a circle with radius %d is %d meters square ' %(radius2, meters)
print(area2)


# 37. Make the following using string formatting methods:

a = 8
b = 6

# 8 + 6 = 14

'Below I show two ways- new style and old style formatting'

new_style1= '{} + {} = {}'.format(a,b, a+b)
print(new_style1)

old_style1 = '%d + %d = %d' %(a,b, (a+b))
print(old_style1)


# 8 - 6 = 2

subtraction = '{} - {} = {}'.format(a,b,a-b)
print("subtraction:", subtraction)

# 8 * 6 = 48

multiplication =  '{} * {} = {}'.format(a,b,a*b)
print(multiplication)

# 8 / 6 = 1.33

division = '{} / {} = {:.2f}'.format(a,b,a/b)   #:.2f
print(division)

# 8 % 6 = 2 

modulus = '{} % {} = {}'.format(a,b, a % b)         

print(modulus)

# 8 // 6 = 1

floor_division = ' {} // {} = {}'.format(a,b, a//b)   # floor division is just division and then round it down 

print(floor_division)


# 8 ** 6 = 262144

exponential = '{} ** {} = {}'.format(a,b,a**b)
print(exponential)


