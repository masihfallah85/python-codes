#minmax of 3 numbers
"""this program find minimum and maximum of three numbers"""

print("enter three numbers")

number_1 = int(input("first number: "))
number_2 = int(input("second number: "))
number_3 = int(input("third number: "))

#assume numebr_1 is both minimum and maximum
minimum = maximum = number_1

#compare maximumm and minimum with second number
if maximum < number_2 :
    maximum = number_2
if number_1 > number_2 :
    minimum = number_2

#compare maximum and minimum with third number
if maximum  < number_3 :
    maximum = number_3
if minimum > number_3 :
    minimum = number_3 

print("minimum: ",minimum,"maximum:",maximum)

#using python's built-in method min and max
print("minimum:",min(number_1,number_2,number_3),"maximum:",max(number_1,number_2,number_3))