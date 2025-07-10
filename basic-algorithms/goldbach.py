#goldbach.py

"""
In this script we should find 2 pairs of prime numebrs which  add up to that number and have lleast distance with themselvs.
"""
#use math library for inf and square root
import math

def prime_checker(n):
    
    """check if a number is prime or not"""

    for  i in range(2,int(math.sqrt(n)) + 1):
        
        if n % i == 0:
            
            return False
    
    else:

        return True


#prompt user to input a number
number = int(input("Enter a number: "))

#validate input
if number % 2 != 0  or number <= 2:

    print("invalid input")

else:
    # create a variable for minimum comprasion and initialize it to infinity
    diffrence_min = math.inf

    #create two variables to save answers
    answer_1 = 0

    answer_2 = 0

    #loop through numbers to find two solutions
    for i in range(number , number // 2 - 1,-1):

        #check if i prime
        if prime_checker(i):

            #store diffrence of numebr and  i and check if it's prime
            diffrence = number - i

            if prime_checker(diffrence):
            
                #check if they have the least diffrence
                if i - diffrence <  diffrence_min:
                
                    diffrence_min = i - diffrence

                    answer_1 = i

                    answer_2 = diffrence

    #print the result
    print(f"two prime numebrs wich create {number} and have least diffrence are {answer_1} and {answer_2}")
