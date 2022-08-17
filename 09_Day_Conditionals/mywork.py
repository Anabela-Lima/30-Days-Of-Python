# Exercises: Level 1---------------------------------------------------------------
'''

Q1.

Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.

'''


user_age = int(input("Enter your age:"))
print("user age", user_age)
if user_age > 18:
    print("You are old enough to drive")
else: print("You still have", (18 - user_age), "years left before you can drive")    


'''

Q2:

 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
 Enter your age: 30
 You are 5 years older than me.

'''
my_age = 12



# just a fun function that determines the number of digits in user_age


def age_digit_counter(user_age):
    str_age=  str(user_age)                 # had to convert to string because int is not iterable i.e. cant do for digit_letter in user_age
    print(type(str_age))
    digit_counter = 0
    for digit_letter in str_age:
         digit_counter += 1
    print("digits in age:", digit_counter)

    return digit_counter
    
    
# a function that checks the year difference and uses the correct form of the word year 
# if difference is 1, word is year (singular form) otherwise its years (plural form)

def age_difference_years_word(user_age):
    years_word = "years"
    difference = user_age-my_age
    if difference == 1:
        years_word = "year"
    else: years_word = "years"
    return years_word



if user_age > my_age:
    print("you are older than me by", user_age - my_age, age_difference_years_word(user_age))
elif user_age is my_age:
     print("oh we are age twins!")    
else: print("You are younger than me")    


'''
Q3:

 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
 Enter number one: 4
 Enter number two: 3
 4 is greater than 3

'''

num1, num2 = int(input("Choose a number:")), int(input("Choose a second number:"))

if num1> num2:
    print('{} is greater than {}'.format(num1, num2))
elif num1<num2:
 print('{} is less than {}'.format(num1, num2))  
else: print('{} is equal to {}'.format(num1, num2))   



'''
Q4: 

 Exercises: Level 2
 Write a code which gives grade to students according to theirs scores:

 80-100, A
 70-89, B
 60-69, C
 50-59, D
 0-49, F

'''

grades = {'Maths':int(input("Enter Maths Grade:")), 'English':int(input("Enter English Grade:")), 'History':int(input("Enter History Grade:"))}

def report(grades):
     print(grades)
     for grades_key in grades:               # for key in grades, which will basically return the value of that key. so if Im on key Maths, it will take the value for that key
        print("grade key:", grades_key)
        if  0< grades[grades_key] < 49:      #  this is like person["first_name"] which will print out their name, so grades[grades_key], first iteration will be grades["Maths"] which will take the value for Maths
             grades[grades_key] = 'F'        # set it to F if key value is between 0 and 49
        elif 50< grades[grades_key] < 59:      
             grades[grades_key] = 'D'       
        elif 60< grades[grades_key] < 69:      
             grades[grades_key] = 'C'       
        elif 70< grades[grades_key] < 89:      
             grades[grades_key] = 'B'       
     else:grades[grades_key] = 'A'
     print(grades)
               
                
          
         



report(grades)

'''
Q5

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

'''

def month_season():
    month= str(input("Enter month:")).lower()
    if month == "january" or month == "february" or month == "December":
        print("It's winter time... BRrrrr🧊")
    elif month == "march" or month == "april" or month == "may":
        print("It's Spring!🌷 ... smell those flowers?")
    elif month == "june" or month == "july" or month == "august":
        print("It's finally Summer! ... icecream anyone? 🌞")
    elif month == "september" or month == "october" or month == "november":
        print("It's Autumn! ... 🍂")
    else: print("I don't recognise that month😥")
        

month_season()


'''
Q6.

The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

'''

fruits = ['banana', 'orange', 'mango', 'lemon']
def fruit_checker():
  
    user_fruit = str(input("Enter a fruit:"))
    
    if user_fruit in fruits:
        print("The fruit exists in the list")
        print(fruits)
    else: print("The fruit does not exist, let's add it") 
    fruits.append(user_fruit)
    print(fruits)
    user_fruit_index = fruits.index(user_fruit)
    user_response= str(input("Do you see your fruit in the list?:")).lower()
    yes = ["yes", "definitely", "of course", "sure", "that's right", "you bet"]
    if user_response in yes:
        print("great! 🌞")    
    else: print("Check again, it should be in position:", user_fruit_index, "😊")    


fruit_checker()

# Exercises: Level 3 ----------------------------------------------------------------

# Here we have a person dictionary. Feel free to modify it!

person={
     'first_name': 'Asabeneh',
     'last_name': 'Yetayeh',
     'age': 250,
     'country': 'Finland',
     'is_married': True,
     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
     'address': {
         'street': 'Space street',
         'zipcode': '02210'
     }
     }


#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:


def person_checker():
    if "skills" in person:
        print("person has skills attribute")
        if "Python" in person["skills"]:                            # this is a nested condition, so given above passed, check the following

             middle_skill_index= int((len(person["skills"])-1)/2)   #need to put int so it can convert from float to an integer value
             print("middle skill index:",middle_skill_index)
             print("person:", person)
             print("middle skill:", person["skills"][middle_skill_index])    
             print("Person has skills property and Python skill")

        else: print("person has skills but not in python")

        # convert skills to set otherwise when comparing, the elements must be identically positioned

        person_skills = set(person["skills"])                       # need to convert the skills which is a list to a set, so I can compare with sets front_end_skills and full_stack_skills
        print("type of person_skills:", person_skills)
        print("skills:",person["skills"])
        front_end_skills = {'JavaScript', 'React'}       
        full_stack_skills= {'JavaScript', 'React', 'Node', 'MongoDB', 'Python'}
        
        # now the comparisons

        if person_skills == front_end_skills :
            print("person has skills property but has only got skill in Javascsript and React. They are a front end developer")
        elif person_skills == full_stack_skills:                    #elif is same as else if (i.e. if the above condition failed, execute the following)
            print("person has skills property and a range of front and back end skills, they are a full stack developer")
        else:(" condition not accounted for")   

    else: print("This person has no skills property")  

    if person["is_married"] is True and person["country"] == "Finland":
        print(person.get("first_name"), person.get("last_name"),"lives in", person.get("country"),".","They are married.")
    else: print(person.get("first_name"),person.get("last_name"), "lives in", person.get("country"),".", "They are not married.")
        

person_checker()            # executing function 
                                