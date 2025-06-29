#palindrome_number

"""in this problem we input a number and check if its palindrom or not"""

#input the number and turn it to a list for using built-in reverse method
number = list(input())

#this assignment uses [:],as its important to createa copy of list rather than a refrecne to it
number_duplicate = number[:]

#use built-in reverse method
number.reverse()

#check equality of two lists
if number == number_duplicate:
    print("YES,the number is palindrome")
else:
    print("NO,the number is nota palindrome")