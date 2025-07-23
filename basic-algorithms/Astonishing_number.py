#Astonishing_number.py

"""
In this script we should find if an integer is astonishing or not.
An astonishing numbe ris a number wich devided to left and right side(a and b),the sum of numbers from left to right(or reverse) become equal to number.
An example is 190,if we devide it to 0 and 19,sum of 0 to 19 become 190.
"""

#Import math for logarithm function
from math import log10

def digit_count(number):

    """This function counts number of digits of a number"""

    return int(log10(number)) + 1

def divide(number,power):

    """This function devides number to left and right based on a power of 10"""

    a = number // (10 ** power)

    b = number % (10 ** power)

    return a,b

def summation(a,b):

    """This function sum numbers within the interval of a and b"""

    if a >= b:

        return sum(range(b,a + 1))
    
    else:

        return sum(range(a,b + 1))
    
#Prompt user to enter a number
number = int(input("Enter a number: "))

#Check the input
if number <= 0 or int(log10(number)) + 1 == 1:

    print("Invalid input")

else:

    #Create two variabels for right and left side
    a = 0

    b = 0
    
    #Create a variable to store power fo 10
    power = digit_count(number) - 1

    #Loop until a becomes the whole number
    while a != number:

        a,b = divide(number,power)

        print(f"a = {a} b = {b} ",end = " ")
        
        #Check if number is astonishing
        if summation(a,b) == number and b >= a:

            print("Ok")

            print("ba_astonishing")

            break

        elif summation(a,b) == number and b <= a:

            print("Ok")

            print("ab_astonishing")

            break
        
        else:
            
            print("X")

            power -= 1

    else:

        print("Number is not astonishing at all")




