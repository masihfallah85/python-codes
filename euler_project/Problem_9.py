#Probem_9.py

"""
There exist excactly 1 pythagoras triplet wich satisfies a + b + c = 1000.
Find the product of a,b,c.
"""

def pythagoras_triplet(a,b,c):

    """This function checks if 3 numbers are pythagoras triplet or not"""

    lst = [a,b,c]

    lst.sort()

    if lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2: 

        return True
    
    else:

        return False
    
#Create a variable for product
product = 1

#Create variables for triplet
a = 0

b = 0

c = 0

#Create a variable as a flag to break the outer loop
flag = False

#Loop through numbers to find the triplet
for i in range(998,0,-1):

    for j in range(1000 - i,0,-1):

        a = i

        b = j

        c = 1000 - a - b

        #Check if they meet the conditions
        if pythagoras_triplet(a,b,c) and a != 0 and b != 0  and c != 0:

            product = a * b * c

            flag = True

            break

    if flag:

        break

#Print the result
print(f"{product} is product of {a},{b},{c} wich are a pythagoras triplet that satisfy a + b + c = 1000")