#digit-seperation 

"""
in this script,we prompt user to enter an integer,then we use the following method to seperate its digits
from right to left without list
"""

#prompting user to input an integer
number = int(input("input an integer: "))

#handle special case that if the number is zero 
if number == 0:
    print(0)
else:

    #create  number_copy and digit_count to count digits,and divisible by 10 for special cases where numebr begins with  zeros at right side
    number_copy = number
    digit_count = 0
    divisible_by_10 = False
    
    #check divisibility by 10 and if it is create a variable to handle zeros at right side later
    if number % 10 == 0:
        divisible_by_10 = True
        number_copy_2 = number

    #count digits of number copy
    while number_copy != 0:
        number_copy //= 10
        digit_count += 1

    #create a divisor to extract the leftmost digit
    divisor = 10 ** (digit_count-1)
    
    #extract and print digits one by one
    while number != 0:
        digit = number // divisor
        print(digit , end = " ")
        number = (number % divisor) * 10
    
    #handle the case wich the number begins with zeros at right side
    if divisible_by_10:

        #exctract and print right side zeros
        while number_copy_2 % 10  == 0:
            print(0,end = " ")
            number_copy_2 //= 10