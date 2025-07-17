#immutable_object_modify_address.py

"""
In this script we demosntrate how memmory address of immutable objects change by modification
"""

def modify_object(number,lst):

    """This fucntion shows simple comprasion of memmory change between mutable and immutable objects"""

    print("Memmory address of number befor modification: ",id(number))
    
    print("Memmory addres of list befor modification: ",id(lst))

    number_copy = number

    lst_copy = lst

    number *= 3

    lst.append(4)

    print("Memmory address of number after modification: ",id(number))
    
    print("memmory address of list after modification: ",id(lst))

    print("Number's address didn't change after modification: ", number is number_copy )

    print("List address didn't change after modification: ",lst is lst_copy)

#Create two variables,one number and one list
number = 5

lst = [2,3]

#demonstrate address change using function
modify_object(number,lst)