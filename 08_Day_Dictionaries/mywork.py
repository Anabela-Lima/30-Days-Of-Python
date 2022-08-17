
# note: You can only use '' not "" in dictionaries
#Create an empty dictionary called dog

dog = {}
#Add name, color, breed, legs, age to the dog dictionary
dog['color'] = 'brown'
dog['breed']= 'Staffie'
dog['legs']= 'four'
dog['age'] = 10

print("dog dictionary:",dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student= {'first_name': 'sonia', 
'last_name':'peters', 
'gender': 'female', 
'age':20, 
'maritial_status': False,
'skills': ['painting', 'dancing', 'cooking', 'singing'],
'country': 'Jamaica',
'city': 'Kingston',
'address': { 
    'street':'235 Portland st',
    'Postcode': 'J154NX'
}}

print("student dictionary", student)

#Get the length of the student dictionary

length_student_dict = len(student)

print("length of student dictionary:", length_student_dict)

#Get the value of skills and check the data type, it should be a list

print("student skills:", student["skills"], "student skills datatype:", type(student["skills"]))

#Modify the skills values by adding one or two skills

last_skill_index= int(len(student["skills"])-1)
print("index of last skill:",last_skill_index)

student["skills"][0], student["skills"][last_skill_index] = "Gymanastics", "netball"

print("modified student dictionary:", student)

#Get the dictionary keys as a list
print("student keys as a list:", student.keys())

print("student values", student.values())

# Change the dictionary to a list of tuples using items() method

print("change key to tuple list:",student.items())

# Delete one of the items in the dictionary

print("deleting first name key value pair in student.Value removed is:", student.pop('first_name'))

# here I am checking if uit has been removed
if 'first_name' not in student:
    print("the key first_name has been removed ")
else: print("the key is still in student")  

# clear the dictionary

student.clear() 

if len(student) == 0:
    print("The dictionary has been cleared")
else: print("clearing failed")


# Delete one of the dictionaries

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}




# since student was cleared above, I will have to redeclare a student object 

student= {'first_name': 'sonia', 
'last_name':'peters', 
'gender': 'female', 
'age':20, 
'maritial_status': False,
'skills': ['painting', 'dancing', 'cooking', 'singing'],
'country': 'Jamaica',
'city': 'Kingston',
'address': { 
    'street':'235 Portland st',
    'Postcode': 'J154NX'
}
}
print("student:", student)

if  '235' in student['address']['street']:
      del student
      print("the number 235 was found in street address, the student dictionary has been deleted")
else: print("the number 235 does not exist in the street address, student dictionary not deleted")    


