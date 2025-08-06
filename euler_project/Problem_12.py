#Problem_12.py

"""
What is the value of the first triangle number to have over five hundred divisors?
A triangular number is a number wich is optained by adding first n natural numbers for example second triangular number is 1+2 = 3
"""

#Import square rot function from math library
from math import sqrt

def triangular_number(n):

    """This function returns nth triangular number"""

    return n * (n + 1) // 2

def divisor_count(number):

    """This function counts number of divisors of an integer"""
    
    count = 0

    for i in range(1,int(sqrt(number)) + 1):

        if number % i == 0:

            count += 2 if i != number // i else  1

    return count 

#Create a variable to hold triangular numbers
number = 0

#Create a variable for terms
term = 1

#Loop through terms to find the triangular number required
while True:

    number = triangular_number(term)

    if divisor_count(number) > 500 :

        break

    term += 1

#Print the result
print(f"{number} is the first triangular number to have 500 divisors")