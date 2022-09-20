
import random
import string as s

print( "\n Question 1.2 \n")

# Write a function which generates a six digit/character random_user_id.

def random_user_id():
 _6_numbers = str(random.sample(range(0,9),6))   # 6 random numbers from 0 to 9
 _6_numbers = _6_numbers.split(",")                        # remove commas
 id= "".join((_6_numbers))                                 # join where there are spaces
 print(id)
random_user_id()

#----------------------------------------------------------------------------------------

print( "\n Question 1.2 \n")


# Modify the previous task. Declare a function named user_id_gen_by_user.
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input
#  is the number of IDs which are supposed to be generated.

def random_user_id_modified(c,n):
 for ids in range(n):
    _6_numbers = str(random.sample(range(0,9),c))    # c random numbers from 0 to 9
    _6_numbers = _6_numbers.split(",")               # remove commas
    id= "".join((_6_numbers))                        # join with where ther are spaces
    print(id)

random_user_id_modified(4,5)

#----------------------------------------------------------------------------------------

def user_id_gen_by_user():
    number_of_chars = int(input("What are the number of characters?"))
    number_of_ids = int(input("How many ids are to be generated?"))
    random_user_id_modified(number_of_chars,number_of_ids)

user_id_gen_by_user()

#----------------------------------------------------------------------------------------
print( "\n Question 1.3\n")


# Write a function named rgb_color_gen. It will generate rgb 
# colors (3 values ranging from 0 to 255 each).

# rgb(125,244,255) - the output should be in this form

def rgb_color_gen():
    my_colours =[]
    for num in range(3):
      x=(random.sample(range(0,250),1))
      my_colours.extend(x)

    rbg ="rbg" 
    my_colours_tuple = str(tuple(my_colours))
    string_list = [rbg, my_colours_tuple]
    final_rbg = ( "".join(string_list))
    print(final_rbg)
    return final_rbg


rgb_color_gen()

#----------------------------------------------------------------------------------------
print( "\n Question 2.1\n")

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after 
# #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

 # ['#a3e12f','#03ed55','#eb3d2b'] 

 # # + digits 0:9 + letters_lowercase: a-f  )

def list_of_hexa_colors():
    hashtag = '#'

    my_nums = []  
    for x in range(10):
        my_nums.append(x)

    print(my_nums)

    my_letters_a_f = list(s.ascii_letters)[:6]
    print("letters a to f:", my_letters_a_f)

    _3_nums= (random.sample(my_nums,3)) 
    _3_letters= (random.sample(my_letters_a_f,3))

    print("3 nums:",_3_nums, "3 letters:",_3_letters)

    for elements in range(1):
        _3_nums.extend(_3_letters) 

    random.shuffle(_3_nums)
    print("shuffled list:", _3_nums)

    _3_nums.insert(0, hashtag)

    no_commas = str(_3_nums).replace(',','')
    no_spaces= (no_commas.replace(' ',''))
    no_apos=(no_spaces.replace("'",""))
    no_open_bracket= (no_apos.replace("[",""))
    final_colour= no_open_bracket.replace("]","")
    print(final_colour)
    return final_colour


list_of_hexa_colors()


print( "\n Question 2.1 solution 2\n")


def hex_colours():
    colour = "#"

    for element in range(6):
        colour+= random.choice((s.hexdigits).lower())
    print(colour)


hex_colours()


#----------------------------------------------------------------------------------------
print( "\n Question 2.2 and 2.3\n")

# Write a function list_of_colors which returns any number of colors in an array.


def list_of_colors(colour_type, times):

    hexa_colours_list = ["hexa","hexadecimal","hex"]
    rgb_colours_list = ["rgb","rgb colour", "rgb color"]

    if colour_type in hexa_colours_list:
        my_hexa_list= []
        for colour in range(times):
         generated_colour = list_of_hexa_colors()
         my_hexa_list.append(generated_colour)
        print("hexa list:", my_hexa_list)

    elif colour_type in rgb_colours_list:
        my_rgb_list = []
        for colour in range(times):
            generated_colour= rgb_color_gen()
            my_rgb_list.append(generated_colour)
        print("rgb list:", my_rgb_list)

     
list_of_colors("rgb",4)