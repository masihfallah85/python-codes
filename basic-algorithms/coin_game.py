#coin_game.py

"""
In this script we have some coins and two players.each player can take 1 or 4 coins each turn and the player taking last coins wins.
Assuming they play optimaly,we should find if player 1 wins or not.
"""

#prompt user to input number of coins
coins = int(input("Enter number of coins: "))

#the game's outcome cycles after each 5 coin,if we have 1,4 or 3 coins player 1 wins else not
if coins % 5 == 1 or coins %  5 == 3 or coins %5 == 4:
    print("Player 1 wins")
else:
    print("Player 2 wins")