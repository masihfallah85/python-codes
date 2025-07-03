#pi-e-series-approximation


"""
in this script we want to approximate mathmatical constants pi and e using Leibniz formula and maclaurin series
"""

#using Decimal for accurate result
from decimal import Decimal

#prompt user to enter term of  the series
term = int(input("enter term of the series: "))

#create variables for pi and e
pi = Decimal(0)
e = Decimal(1)

#create a variable for factorial used in e maclaurin series
facotrial = 1

#calculate pi using this loop
for k in range(term):
    pi += Decimal((-1) ** k / (2 * k + 1))

#apply 4 multiplier to pi
pi *= 4

#use this loop to calculate e
for k in range(1,term):
    facotrial *= k
    e += Decimal(1 / facotrial)

#print the results
print(f"approximation of pi by {term} term of Leibniz formula is : {pi}")
print(f"approximation of e by {term} term of maclaurin series is : {e} ")