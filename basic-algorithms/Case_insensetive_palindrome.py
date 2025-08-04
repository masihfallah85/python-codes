#Case_insensetive_palindrome.py

"""
In this script we check if a string is palindrome or not without case sensetivity\
"""

def palindrome(string):

    """This function checks if a string is palindrome or not"""

    lst = []

    for i in string:

        lst.append(i)

    lst_reverse = lst[::-1]

    for i,j in zip(lst,lst_reverse):

        if i.lower() != j.lower():

            return False
        
    else:

        return True
    
#Prompt user to input a string
string = input("Enter a string: ")

#Print the result
if palindrome(string):

    print(f"{string} is palindrome")

else:

    print(f"{string} is not palindrome")