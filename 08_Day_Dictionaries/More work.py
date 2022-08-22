# Consider the following list containing 2 dictionaries. 
# Remember, lists are ordered lists with a numeric index and dictionaries are labeled lists where each key denotes its value.
# In a way, think of each dictionary's key as a variable that holds the value on the right of the colon symbol.

fruits = [
    {
        "item": "apple",
        "quantity": 5,
        "price": 0.95
    },
    {
        "item": "orange",
        "quantity": 7,
        "price": 0.99
    }
]

print("fruits",fruits)

# How do we access the first dictionary in the list?


first_dictionary = fruits[0]

print("first dictionary:", first_dictionary)

# How would we get the number of apples?

num_apples_fd = fruits[0]['quantity']
print("quantity of apples in first dictionary:", num_apples_fd)

# How would we determine the total spent on apples where we multiply price * quantity?

total_spent_apples = (fruits[0]['quantity'])*(fruits[0]['price'])
print("total spent on apples:£",total_spent_apples)

# What's one way to determine the total quantity of all items in the fruist list of dictionaries?

total = fruits[0]['quantity']+ fruits[1]['quantity']

print("total quantity using simple addition:", total)

# What about if we have a longer list than only two? What if we need this to be programmatic? Use a loop!

total = 0
for object in fruits:
    total = total + object['quantity']

print("total quantity using loops:", total)

# What's one way to determine the total spent on both apples and oranges? (this is the "brute force" way)

total_apples_Oranges = 0
for object in fruits:
        total_apples_Oranges = total_apples_Oranges + (object['quantity']* object['price'])

print("total of apples and oranges: £", total_apples_Oranges)
   


print(" ")

# How would we determine the average price spent per item?

total_spent = 0
total_quantity= 0


for object in fruits:

    quantity = object["quantity"]
    print("Fruit quantity:", quantity)

    price = object["price"]
    print("Fruit price:£", price)

    total_spent= total_spent + (quantity * price)
    print("total spent:", total_spent)
    print(quantity)
    
    total_quantity = total_quantity + object["quantity"]


print( "total  fruit quantity: ", total_quantity)
average = (total_spent/total_quantity)
print("Average price spent on oranges and apples is: £",'{:.2f}'.format(average))    # '{:.2f}'.format(x) to convert to 2 dp only


#--------------- Next Question --------------------------


print("\nNext Exercise:\n")

vegetables = [
    {
        "item": "apple",
        "quantity": 5,
        "price": 0.95
    },
    {
        "item": "orange",
        "quantity": 7,
        "price": 0.99
    }
]


