#Problem_10.py

"""
What's sum of prime numbers below 2 million?
"""

#Import square root function from  math library
from math import sqrt

def prime(number):

    """This function checks if a number is prime or not"""

    for i in range(2,int(sqrt(number)) + 1):

        if number % i == 0:

            return False
        
    else :

        return True
    
#Create a variable for sum of primes
total = 0

#Loop through 2 to 2 million
for i in range(2,2_000_000):

    #Check if i is prime
    if prime(i):

        total += i

#Print the result
print(f"{total} is sum of all primes from 1 to 2_000_000")