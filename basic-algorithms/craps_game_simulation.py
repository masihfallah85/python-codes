#craps_game_simulation.py

"""
You roll two six-sided dice, each with faces containing one, two, three, four, five
 and six spots, respectively. When the dice come to rest, the sum of the spots on the
 two upward faces is calculated. If the sum is 7 or 11 on the first roll, you win. If
 the sum is 2, 3 or 12 on the first roll (called “craps”), you lose (i.e., the “house”
 wins). If the sum is 4, 5, 6, 8, 9 or 10 on the first roll, that sum becomes your
 “point.” To win, you must continue rolling the dice until you “make your point”
 (i.e., roll that same point value). You lose by rolling a 7 before making your point. 
"""

#import random module to simulate dice roll
import random

#create two variables for two dices and initialize them with first throw
dice_1 = random.randrange(1,7)

dice_2 = random.randrange(1,7)

#create a variable for game status
game_status = ""

#create a variable to sum dice values
sum_of_values = dice_1 + dice_2

#check game status on first roll
if sum_of_values in (7,11):

    game_status = "Won"

elif sum_of_values in (2,3,12):

    game_status = "Lost"

else:

    game_status = "continue"
    
    #create a variable for point
    point = sum_of_values

    #show point of player
    print("my point: ",point)

#loop while game status is continue
while game_status == "continue":
     
    #roll dices again and sum their values
    dice_1 = random.randrange(1,7)

    dice_2 = random.randrange(1,7)

    sum_of_values = dice_1 + dice_2

    #check if player won or loses or should roll again
    if sum_of_values == point:

        game_status = "Won"
    
    elif sum_of_values == 7:

        game_status = "Lost"

#print result of the game
print("player Won" if game_status == "Won" else "player Lost")