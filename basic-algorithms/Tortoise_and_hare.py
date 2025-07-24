#Tortoise_and_hare.py

"""
In this script we simulate classic race of tortoise and hare with following description:
Our contenders begin the race at square 1 of 70 squares. Each square represents a
 position along the race course. The finish line is at square 70. The first contender to reach
 or pass square 70 is rewarded with a pail of fresh carrots and lettuce. The course weaves its
 way up the side of a slippery mountain, so occasionally the contenders lose ground
 A clock ticks once per second. With each tick of the clock, your application should
 adjust the position of the animals according to the rules in the table below. Use variables
 to keep track of the positions of the animals (i.e., position numbers are 1–70). Start each
 animal at position 1 (the “starting gate”). If an animal slips left before square 1, move it
 back to square 1.
"""

#Import randrange for random movments
from random import randrange

def tortoise_movment(tortoise_position):

    """This function simulate tortoise's movment"""

    move_type = randrange(1,11)

    if 1 <= move_type <= 5:

        return tortoise_position + 3
    
    elif 6 <= move_type <= 7:

        return tortoise_position - 6
    
    elif 8 <= move_type <= 10:

        return tortoise_position + 1
    

def hare_movment(hare_position):

    """This function simulate hare's movment"""  

    move_type = randrange(1,11) 

    if 1 <= move_type <= 2:

        return hare_position
    
    elif 3 <= move_type <= 4:

        return hare_position + 9
    
    elif move_type == 5:

        return hare_position - 12
    
    elif 6 <= move_type <= 8 :

        return hare_position + 1
    
    elif 9 <= move_type <= 10:

        return hare_position - 2

#Create variables for tortoise and hare position
tortoise_position = 1

hare_position = 1

#Print starting prompt
print(" BANG !!!!!")

print("AND THEY'RE OFF !!!!!")

#Loop until at least one of them reach the end
while tortoise_position < 70 and hare_position < 70:

    tortoise_position = tortoise_movment(tortoise_position)
    
    hare_position = hare_movment(hare_position)
    
    #Check if they go off the map
    if tortoise_position < 1:

        tortoise_position = 1

    
    if hare_position < 1:

        hare_position = 1
    
    #Print their position
    for i in range(1,71):

        print("_" if i != tortoise_position else "T",end ="")

    print()

    for i in range(1,71):

        print("_" if i != hare_position else "H",end = "")

    print()

#Print winner
if tortoise_position >= 70 and hare_position >= 70:
    
    print("Tie")

elif tortoise_position >= 70:

    print("Tortoise winned")

else:

    print("Hare winned")
