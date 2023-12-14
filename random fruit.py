# This program asks users if they want fruit
# Returns a random fruit from the array
import random

fruits = ["pear", "banana", "strawberry", "plum", "grape"]
#Counter for number of times fruit question has been asked
asks = 0
no = 0
while asks <3:
# Asks user for their input on fruit.
    fruit_q = input("Would you like a random fruit? Yes or No? ")
    #set string to lower case to disregard case sensitivity
    if fruit_q.lower() == "yes":
        print("Here is a " + random.choice(fruits) + " for you.")
        asks += 3
    #If user enters no loop with suggestion    
    elif fruit_q.lower() == "no":
        print("You should eat fruit.")
        asks += 1
        no += 1
    #User could possibly enter something else, so cath the edge case and give recommendation anyway.    
    else:
        print("I don't understand that. But here is a " + random.choice(fruits) + " for you")
        asks += 3
# If the user repeatedly says no to fruit
if no == 3:
    print("You need fruit, so here is a " + random.choice(fruits) + " for you.")
        
            