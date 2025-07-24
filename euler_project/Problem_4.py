#Problem_4

"""
What's the largest palindrome made from product of two 3-digit numbers?
"""

def palindrome(number):

    """This function checks if a number is palindrome or not"""

    string_number = str(number)

    string_number_reversed = string_number[::-1]

    if string_number == string_number_reversed:

        return True
    
    else:

        return False
    

#Create a variable to store largest palindrome,assume it's 0 for now
largest = 0

#Loop through 3 digit numbers to find largest palindrome
for i in range(100,1000):

    for j in range(i,1000):

        if palindrome(j * i) and j * i > largest:

            largest = j * i

#Print the result
print(f"{largest} is largest palindrome made from product of two 3-digit numbers")