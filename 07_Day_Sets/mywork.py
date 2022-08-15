# Set is a collection of unordered items, so you cannot be sure in which order the items will appear.
# set elements are unique i.e. only appear once in the set, cant be repeated
# and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.
# * Note: Sets cannot be modified once created,  but we can remove items and add new items.

'''

.add() - to add items to the set
.update(["item1", "item2",...]) - add multiple items to a set, or you can do 
set1.update(my_tuple) -add a tuple to a set
set1.update(my_set) - join two sets
st1 = st1.union(st2) -join two sets

note: pop method removes a random item from the list and returns it

st1.insersection(st2) - intersection between two sets- i.e common elements

st2.issubset(st1) - checks if all elements of two comes from set 1- boolean output
st1.isssuperset(st2) - checks if 1 is superset (parent) of set 2

st2.difference(st1)- what elements are different when two sets are compared, if no difference, output = set()

st2.symmetric_difference(st1)- returns a set with items from both sets, except items which are common in the two:  (A\B) ∪ (B\A)

st2.isdisjoint(st1)- checks whether sets have common items, if they are disjoin => no common items

'''


# sets
from ntpath import join
from posixpath import split


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1---------------------------------------

# Find the length of the set it_companies
length_it_companies = len(it_companies)
print("length of it companies set:",length_it_companies)

# Add 'Twitter' to it_companies

it_companies.add("Twitter")
print("It companies with Twitter:", it_companies)

# Insert multiple IT companies at once to the set it_companies

more_it_companies = {"AnaTech", "ItechNew", "SaturnTech", "Futurex", "MoreTech"}
it_companies.update(more_it_companies)
print("updated it companies", it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove("AnaTech")

# just a quick check to see if its been removed: 
print("AnaTech" in it_companies)  # False

# What is the difference between remove and discard

# the difference between remove and discard is that, remove will raise an exception, if item to be removed does not exist, discard will not.

# Exercises: Level 2
# Join A and B

joined_A_B = A.union(B)
print("Set A and B joined: ", joined_A_B)  # note how sets A and B despite being joined, the length =/ A + B , this is because sets cannot have duplicate elements

# Find A intersection B

intersection_A_B = A.intersection(B)
print("Intersection of A and B:", intersection_A_B)

# Is A subset of B

print("A subset B:" , A.issubset(B))  # True


# Are A and B disjoint sets

# disjoint means no common items, I expect this to be false, because A and B have an intersection which implies commonality 

print("A and B disjoint:", A.isdisjoint(B))   # False

# Join A with B and B with A

A_B = A.union(B) 
print(A_B)
B_A= B.union(A)
print(B_A)

difference= A_B.difference(B_A)
print(difference)                           # No difference- the elements remain the same the same

# note however, if you do 

print(A_B is B_A)         # may be false because sets are unordered, so elements can be in different positions, so when compared with is, it is likely to be false
# because we are asking is A_B identical to B_A



# What is the symmetric difference between A and B  # solved above
# answer is no difference

# Delete the sets completely
del (A_B, B_A)
# print(A_B, B_A)         # not defined as expected since we deleted the sets

# Exercises: Level 3

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?

ages_to_set = set(age)
print("ages to set:", ages_to_set)

# Explain the difference between the following data types: string, list, tuple and set

# A string is a sequence of characters
# list: a datastructure in python, denoted by [] that is ordered and mutable (can be changed)
# Set: A datastructure in python denoted by {} that is unorderd, immutable with a collection of unique elements. Although a set is immutable, we can still add or remove items

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

# declare the string
string = "I am a teacher and I love to inspire and teach people"

# split the string 
split_string= (string.split(" "))

# convert the split string to a set 

string_set = set(split_string)
print(string_set)

# since a set does not allow any repeated elements, we can simply count the words to find the number of unique words 

unique_words = len(string_set)

print("The number of unique words are", unique_words)



