#perfect-number.py

"""
In this script user inputs a number and we should tell if its perfect or not.
A number is perfect if it's equal to sum of all it's proper devisors
"""

#prompt user to input a number
number = int(input("Enter a number: "))

#create a variable for sum of divisors
total = 0

#loop through  1 to half of number to find it's devisors
for divisor in range(1,number // 2 + 1):

    #check if it's actually number's devisor
    if number % divisor == 0:
        
        #add devisor to sum
        total += divisor

#check if it's a perfect number and print the result
if total == number:
    
    print(f"{number} is a perfect number")

else:
    print(f"{number} is not a perfect number")
