#Bubble_sort.py

"""
In this script we sort a list in ascending order with bubble sort.
"""

def bubble_sort(lst):

    """This function sorts a list with bubble sort"""

    for i in range(len(lst) - 1):

        for j in range(len(lst) - 1):

            if lst[j] > lst[j + 1]:

                lst[j] , lst[j+1] = lst[j + 1] , lst[j]

    return lst

#Prompt user to input a list of numbers
string = input("Enter list of numbers: ").split()

lst = list(map(lambda x : float(x),string))

#Print the result
print(f"{bubble_sort(lst)}  is sorted verision of the list using bubble sort")