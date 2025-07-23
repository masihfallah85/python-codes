#Problem_3

"""
What is largets prime factor of 600851475143?
"""

#Import math for sqrt function
from math import sqrt

def prime(number):

    """This function checks if a number is prime"""

    for i in range(2,int(sqrt(number)) + 1):

        if number % i == 0:

            return False
    else:

        return True
    
#Create a variable for largest prime factor,assume it's 2
prime_factor = 2

#Loop through 2 to square root of number to find largest prime factor
for i in range(2,int(sqrt(600_851_475_144)) + 1):

    #Check if i is divisor of 600_851_475_143 and is prime
    if 600_851_475_143 % i == 0  and prime(i):

        #Compare it to previous result
        if i > prime_factor:

            prime_factor = i

#Print result
print(f"largest prime factor of 600851475143 is {prime_factor} ")