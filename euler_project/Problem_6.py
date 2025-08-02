#Problem_6.py

"""
What's diffrence of sum of squares and square of sum of first one hundred natural number?
"""

#Calculate square of sum
square_of_total = (sum(list(range(1,101)))) ** 2

#Calculate sum of squares
total_of_squares = sum(map(lambda x : x ** 2,list(range(1,101))))

#Print the result
print("Diffrence of  sum of squares and square of sum from 1 to 100 is:",square_of_total - total_of_squares)