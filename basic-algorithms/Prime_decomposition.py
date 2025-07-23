#Prime_decomposition.py

"""
In this script we prompt user to input a number bigger than 1 and we decompose it to it's prime factors.
"""
#Import math for square root function
from math import sqrt

def prime(number):

    """This funtion check if a number is prime or not"""

    for i in range(2,int(sqrt(number)) + 1):

        if number % i == 0:

            return False
    
    return True

def power(number,base):

    """This function return power of base wich result in number """
    
    expotent = 1

    while number % base == 0:

        expotent += 1

        base **= expotent
    
    return expotent - 1

#Prompt user to input a number
number = int(input("Enter a number bigger than 2: "))

#Check input
if number < 2:

    print("Invalid input")

#Check if number is prime
elif prime(number):

    print(number)
    
else:

    #Create a variable to correctly show decomposition by seperating first factor
    is_first = True

    #Loop through 2 to square root of number to show it's prime decomposition
    for i in range(2,int(sqrt(number)) + 1):

        #Check if i is divisor of number and a prime
        if number % i == 0  and prime(i):

            #Store the power of i wich result in  number in a variable
            expotent = power(number,i)

            #Print the result
            if is_first:

                print(f"{i} ** {expotent}",end = " ")

                is_first = False
            
            else:

                print(f"* {i} ** {expotent}",end = " ")