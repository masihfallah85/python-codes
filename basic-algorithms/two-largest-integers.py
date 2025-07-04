#two-largest-integers

"""
in this simple script we should find two largest integers from 10 integers without functions or data structurs
"""

#prompt user to input first integer
number  = int(input("input an integer: "))

#create max and second_max and put value of first integer in them
max = second_max = number

#use for loop to input other 9 integers and find two largest of them all
for count in range(9):
    
    #prompt user to input an integer
    number = int(input("input an integer: "))
    
    #if its bigger than max one,then replace second largest with max and then replace max with the number bigger than it
    if number > max:
        second_max = max
        max = number

#print the result
print("largest: ",max,"second largest: ",second_max)