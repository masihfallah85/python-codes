#palindrome-integer

"""
in this script we check if a integer is palindrome without using list
"""

#prompting user to input a number
number = int(input("enter an integer: "))

#creating two copies of number for creating it's reverse and coutning its digits
number_copy = number
 
#create a variable to store reverse form of the number
reverse_number = 0 

#construct reverse form of the number
while number_copy != 0:
    digit = number_copy % 10
    number_copy //= 10
    reverse_number = (reverse_number * 10) +digit

#check for palindrome
if reverse_number == number:
    print(f"{number} is palindrome")
else:
    print(f"{number} is not palindrome")