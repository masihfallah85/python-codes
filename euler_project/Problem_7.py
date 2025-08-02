#Problem_7.py

"""
What's the 10_001st prime number?
"""

#Import square root function from math library
from math import sqrt

def prime(number):

    """This function check if a number is prime or not"""

    for i in range(2,int(sqrt(number)) + 1):

        if number % i == 0:

            return False
    
    else:

        return True
    
#Create a variable for index
index = 0

#Create a variable to hold numbers
number = 2

#Create a variable for answer
answer = 0
#Loop through numbers while index is not 10_001
while index != 10_1001:

    #Check if number is prime
    if prime(number):

        index += 1

        if index == 10_001:

            answer = number

    #Go to next number
    number += 1

#Print the result
print(f"{answer} is the 10_001st prime number")