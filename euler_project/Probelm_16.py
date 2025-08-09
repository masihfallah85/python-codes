#Problem_16.py

"""
What's sum of digits 0f 2 ** 1000?
"""

def digits_sum(number):

    """This function sums the digits of a number"""

    sum = 0

    for i in str(number):

        sum += int(i)

    return sum

#Print the result
print(f"Sum of digits 0f 2 ** 100 is {digits_sum(2 ** 1000)}")