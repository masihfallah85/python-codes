#Set_operations.py

"""
In this scripts we have this sets:
F = set of fiction books

𝑁
N = set of non-fiction books

𝐻
H = set of books currently on hold by a reader
then if we have this: F={101,102,103,104}N={103,105,106,107}H={102,103,106}

find the books wich are both fiction and non ficiton,books that are available and cartesian product of f and h.
verify if H ⊆ F ∪ N.
"""

def cartesian(set_1,set_2):

    """This function creates cartesian prodcut of two sets"""

    product = set()

    for member in set_1:

        for member_2 in set_2:


            product.add((member,member_2))
    
    return product

def logical_formula(H,F,N):

    """This function verifies the  formula H ⊆ F ∪ N """

    return H <= (F | N)

#Create sets
F = {101,102,103,104}

N = {103,105,106,107}

H = {102,103,106}

#Find wich books are fiction and non-fiction
print(f"Books {F & N} are/is both fiction and non-fiction")

#Find wich books are available 
print(f"Books {(F | N) - H} are,is available")

#Find cartesian product of f and h
print(f"Cartesian product of {F} and {H} is {cartesian(F,H)}")

#Verify H ⊆ F ∪ N
print(f"Formula H ⊆ F ∪ N is {logical_formula(H,F,N)}")