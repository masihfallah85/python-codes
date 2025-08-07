#Problem_15.py

"""
In a 20 in 20 grid wich we can move right or down,how many possible ways we have to go to buttom right?
"""

#Import factoriel function from math library
from math import factorial

def ways(n):

    """This function  counts number of ways to go to buttom left of a n in n grid"""

    return factorial(2 * n) // (factorial(n) * factorial(n))

#Print the result
print(f"number of ways to go buttom right of a grid with right-down moves is {ways(20)}")