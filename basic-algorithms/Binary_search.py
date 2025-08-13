#Binary_search.py

"""
In this script we implement binary search algorithm
"""

def binary_search(lst,key):

    """This function finds index of a key value using binary search"""

    lower_bound = 0

    upper_bound = len(lst) - 1

    middle = (lower_bound + upper_bound) // 2

    while lower_bound <= upper_bound:

        if key == lst[middle]:

            return middle
        
        elif key > lst[middle]:

            lower_bound = middle + 1

            middle = (lower_bound + upper_bound) // 2

        elif key < lst[middle]:

            upper_bound = middle - 1

            middle = (lower_bound + upper_bound) // 2

    return -1

#Prompt user to enter a list
string = input("Enter a list of numbers: ").split()

lst = [float(i)  for i in string]

lst.sort()

#Prompt user to enter a key
key = float(input("Enter the value you look for: "))

#Print the result
if binary_search(lst,key) == -1:

    print(f"Value {key} doesn't exist in the list")

else:

    print(f"{key} is at index {binary_search(lst,key)} in the sorted  list")