
import random

print("\n Question 1.1 \n")
# Write a function which generates a six digit/character random_user_id.

def random_user_id():
 _6_numbers = str(random.sample(range(0,10),6))   # 6 random numbers from 0 to 10
 _6_numbers = _6_numbers.split(",")               # remove commas
 id= "".join((_6_numbers))                        # join where there are spaces
 print(id)
random_user_id()

