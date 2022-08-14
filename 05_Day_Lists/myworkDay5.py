# List: is a collection which is ordered and changeable(modifiable). Allows duplicate members. can have different types     []
# Tuple is collection= ordered + unchangeable + unmodifiable(immutable). Allows duplicate members.  ()
# Set is collection= unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
# Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members. its like an object. 

#------------------------- Exercises--------------------------------------


# Declare an empty list

from audioop import avg
from ntpath import join
from statistics import mean, median


colours = []

# Declare a list with more than 5 items
colours= ["red", "blue", "yellow", "pink", "orange", "green"]

# Find the length of your list

print(len(colours))

# Get the first item, the middle item and the last item of the list

first_item, middle_item, last_item = colours[0], colours[2], colours[5]
print("first item:", first_item,"middle_item:", middle_item, "last_item:", last_item)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["Ana", 100, 180, "married", "123 Saturn Way"]
print(mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies= ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# Print the list using print()
print(it_companies)

# Print the number of companies in the list

length_it_companies = len(it_companies)

print("length of it_companies: ", length_it_companies)

# Print the first, middle and last company

first_item_it_companies = it_companies[0]
print(first_item_it_companies)

# Print the list after modifying one of the companies

it_companies[4] = "AnaInc"

print(it_companies)

# Add an IT company to it_companies

it_companies.append("IT company")
print(it_companies)

# Insert an IT company in the middle of the companies list

middle = int((length_it_companies -1)/2)
print("middle:",middle)

it_companies.insert(middle, "SaturnIT")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[0] = it_companies[0].upper()      # its reassigning item in index 0 to be uppecase
print(it_companies)

# Join the it_companies with a string '#;  '

print("#;".join(it_companies))

# Check if a certain company exists in the it_companies list.

print("AnaInc exists:", "AnaInc" in it_companies)
print("JupiterInc exists:" , "JupiterInc" in it_companies)

# Sort the list using sort() method

it_companies.sort()   # will put items in ascending order 
print(it_companies)   # note you have to perform this in 2 steps- otherwise it will print NONE

# Reverse the list in descending order using reverse() method

it_companies.sort( reverse = True) 
print(it_companies)

# Slice out the first 3 companies from the list

# lets reverse the list back to normal first

it_companies.sort(reverse = False)

print("Before slicing:", it_companies)
del it_companies[0:3]                                                               # we use del when we want to remove a specific index
print("Sliced first 3 it companies:", it_companies)

# Slice out the last 3 companies from the list

print("It companies before slice last 3:",it_companies)

print("Before removing last 3:", it_companies)
del it_companies[3:]                                                                # delete from index 3 onwards
print("After removing last 3:", it_companies)

# Slice out the middle IT company or companies from the list


print("Before slicing middle:", it_companies)
middle_it_company = int((len(it_companies) -1 )/2)
print("middle IT company:", middle_it_company)
print("After slicing middle, removed: ",it_companies.pop(middle_it_company) ,",", "Companies left:", it_companies)


# Remove the first IT company from the list

print("it company before:", it_companies)
it_companies.pop(0)
print("it companies after remove first", it_companies)

# Remove the middle IT company or companies from the list

# let me just add a few more companies in 
print("It companies before adding more:", it_companies)
extra_companies = ("NewTech", "Futurex","Isolo")
it_companies.extend(extra_companies)
print("It_companies after adding more companies", it_companies)

middle_ItCompany_2 = int((len(it_companies) -1)/2)    # the index was 1.5 but floats cannot be used as index so I convert it to an int, resulting in 1
print("middle company index:", middle_ItCompany_2)
it_companies.pop(middle_ItCompany_2)
print("it_companies after removed middle", it_companies)

# Remove the last IT company from the list

print("removed last:", it_companies.pop(),  "it companies left:" , it_companies)

# Remove all IT companies from the list

it_companies.clear()
print("cleared it_companies:",it_companies)

# Destroy the IT companies list
del it_companies
# print(it_companies) # "NameError: name 'it_companies' is not defined", as expected 


# Join the following lists:

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React','Redux']
back_end = ['Node',' Express', 'MongoDB']

joined_list = front_end + back_end
print(joined_list)


# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.


full_stack =joined_list.copy()
print("Full stack: ",full_stack)

# Exercises: Level 2
# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()                     # note, we cant reassign a variable when we use a the sortmethod because sort() returns None

# to get the sorted list with sort() we must print the original variable 

print("using sort method and printing original vairiable:", ages)

# But, if we did want to reassign the variable what we can do is use the method sorted() 
# this allows us to reassign the list because sorted method returns the sorted list 

sorted_ages = sorted(ages)
print("using sorted method", sorted_ages)

# in conclusion- use the original variable. sort() and print the original list when using sort(),
# but use new_variable = sorted(original variable) and print the new list when using sorted() when you want to sort the list
# but not change the original list, hence the declaration of a new varible.


# Add the min age and the max age again to the list

print("ages array:", ages)
max_age, min_age = max(ages), min(ages)
print("max age:", max_age, "min age:", min_age)

# Find the median age (one middle item or two middle items divided by two)

median_age = int(median(ages))                  # didnt want it as a float so converted to int
print("median age:", median_age)

# Find the average age (sum of all items divided by their number )

average_age = int(mean(ages))
print("average age", average_age)

# Find the range of the ages (max minus min)

range = max_age -min_age
print("range: ", range)

# Compare the value of (min - average) and (max - average), use abs() method

one = min_age - average_age
two = max_age - average_age
print("absolute comparison i.e. min max average:", abs(two - one))
# Find the middle country(ies) in the countries list

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

middle_country = int(((len(countries)) -1)/2)
print("middle country index",middle_country)
print("middle country:", countries[middle_country])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.

print("countries list:", countries)
first_half, second_half = countries[0:middle_country], countries[middle_country:]
print("first half:", first_half)
print("second half:", second_half)
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

first_country, second_country, third_country, *rest = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

print("first country:", first_country)
print("second country:", second_country)
print("third country:", third_country)

rest_separated_with_commas = rest
print("rest of the countries:", rest)


# a one line print

print("ONE LINE PRINT-> " "first country:", first_country, ", second country: ", second_country, ", third country:", third_country, ", rest of the contries:", rest)