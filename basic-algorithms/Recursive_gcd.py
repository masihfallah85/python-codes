#Recursive_gcd.py

"""
In this script we find greatest common divisor of two numbers
"""

def gcd(number_1,number_2):

    """This function finds greatest common divisor of two numbers"""

    if number_1 %  number_2 == 0:

        return number_2
    
    else :

        return gcd(number_2,number_1 % number_2)
    
#Prompt user to input two numbers
number_2 , number_1  = input("Enter two numbers: ").split()

#Sort the numbers
tple = (int(number_2) , int(number_1))

number_2 , number_1 = sorted(tple)

#Print the result
print(f"{gcd(number_1,number_2)} is greatest common divisor of {number_1} and {number_2}")
