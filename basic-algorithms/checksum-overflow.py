#checksum-overflow

"""
In this script we simulate a checksum system wich represent a string with its checksum limited to 8 bites.We should calculate how many times it overflows from 8
bites in cheksum process as well as show 8 bits of final checksu mresult without using fucntions or strings
"""

#prompt user to enter number of characters
number_of_characters = int(input("enter number of characters: "))

#creat a variable to sum ascii values of characters
sum = 0

#create a variable to count number of times we encounter overflow in checksum process
count_overflows = 0

#create a variable to store eahc character
charcter = ""

#loop throug number of characters to get each charcater
for number in range(number_of_characters):

    #prompt user to input character
    charcter = input("enter a character: ")

    #add its ascii value to sum
    sum += ord(charcter)

    #check if sum is equal or greater than 256(more than 8 bites) to differentiate 256 from sum and increase number of overflows by 1
    if sum >= 256:
        sum -= 256
        count_overflows += 1

#print the result
print("checksum final value: ",bin(sum))
print("number of overflows: ",count_overflows)