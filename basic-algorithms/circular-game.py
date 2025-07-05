#circular-game

"""
This script simulates a circular game with n players seated in a circle.
Starting from player 1, every kth player takes the next turn.
The goal is to determine how many turns it takes before it is player 1's turn again.
"""

#prompt user to enter number of people
people = int(input("enter number of people: "))

#prompt user to  enter next person's distance from current one for each turn
turn = int(input("enter next person's distance from current one each turn: "))

#create a variable for number of turns it takes to first person's turn again,assume it's one for now
number_of_turns = 1

#create a variable for mutliplier for later use and assume its two
multiplier = 2

#create a variable to store number of peoples for mosification
copy_of_people = people
#use this while loop to find a peopl's mutliplier wich is divisable by turn number
while copy_of_people % turn != 0:
      copy_of_people = people * multiplier
      multiplier += 1

#then find result of divison on copy_of_people and turns to see how many turns it takes
number_of_turns = copy_of_people // turn

#print the result
print(f"number of turns it takes to first person's turn again is {number_of_turns}")