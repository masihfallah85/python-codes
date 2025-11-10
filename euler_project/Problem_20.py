#Problem_20

"""
Find sum of digits of 100!
"""

def factoriel(n):

    """This function finds factoriel of n"""

    total = 1

    if n == 0 or n == 1:

        return 1
    
    else:

        for i in range(2,n + 1):

            total *= i

        return total
    
def sum_digits(number):

    """This functions adds digits of a number together"""

    string = str(number)

    total = 0

    for i in string:

        total += int(i)

    return total

#Print the result
print(f"Sum of digits of 100! = {factoriel(100)} = {sum_digits(factoriel(100))}")