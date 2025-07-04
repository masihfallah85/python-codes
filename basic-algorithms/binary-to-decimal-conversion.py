#binary-to-decimal-conversion

"""
in this script,user inputs an integer coposed of 1 and 0 acting as a binary number,we should turn it to its decimal counterpart
(without use of fucntions or data structures)
"""

#prompt user to input binary number
binary_number = int(input("enter a binary number: "))

#create a copy of binary number so we don't change it to show it in output
binary_number_copy = binary_number

#create a variable to show its decimal counterpart
decimal_number = 0

#create a variable to handle powers of 2
power = 0

#create variable to handle binary digits
digit = 0

#using this while loop logic to calculate its decimal counter part
while binary_number != 0:
    digit = binary_number % 10
    decimal_number += (2 ** power) * digit
    binary_number //= 10
    power += 1

#print the result
print(f"decimal form of binary number {binary_number_copy} is : {decimal_number}")