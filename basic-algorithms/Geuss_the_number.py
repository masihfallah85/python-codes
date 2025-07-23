#Geuss_the_number.py

"""
In this script we implement a simple game of geussing a number between 1 to 1000.
"""

#import randrange from random library to generate a random number
from random import randrange

def game_result(geuss,number):
    
    """This function returns game results"""

    if geuss < number:

        return "Too low","No"
    
    elif geuss > number:

        return "Too high","No"
    
    else:

        return "Correct","Yes"
    
#Create a variable for geussed number
geuss = 0

#Create a variable for result of the game
result = "No"

#Create a variable to store game status
status = "Continue"

#Create a variable for hint
hint  = ""

#Create a variable for storing a random number between 1 to 1000
number = randrange(1,1001)

#Continue game while user doesn't want to finish game
while status == "Continue":

    #Prompt user to  Geuss a number between 1 to 1000
    geuss = int(input("Guess a number between 1 to 1000: "))

    #Check input
    if geuss < 1 or geuss > 1000:

        print("Invalid input,it should be between 1 to 1000")

    else:
        
        #Show geuss result
        hint , result = game_result(geuss,number)
        
        print("Result: ",result)

        print("Hint: ",hint)

        #Check if user answered correctly
        if result == "Yes" :

            #Prompt user to finish or continue
            status = input("Do you want to play again?: ")

            if status == "Yes":
                 
                result = "No"

                number = randrange(1,1001) 
                
                status = "Continue"
            
            else:

                status = "Finish"