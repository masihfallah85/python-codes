#Linear_search

"""
In this script we search for an element in an array by linear_search by checking all elements of array.by loop invariant analysis,first we check first index A[1],
if it's the inteded key loop terminates and otherwise we go to next index,when loop goes out of bound(ie n + 1 index) then all the idnexes are cheked,and if it doesn't
exist in the array we return "-1" a flag.in floyd_hoar logic:

{True}A[i] = x  or A[i] != x {i := i + 1 if A[i] != x or return i}/{i = 0 and x}A[i] != x or A[i] != x{-1 if for all i x != A[i] or x if there exist an i wich A[i] = x}

"""

def linear_search(array,x):

    """This function search for an element in an array with linear_search"""

    for i in array: #cost = c1 times = n + 1

        if x == i: #cost = c2 times = n

            return i 
        
    else : #cost = c3 times = 1

        return -1 
    
#Creating an example array 
lst = [1,2,3,4,5,6,7,8,9,10]

print(linear_search(lst,8))

"""
Best case happents when the first element is our target wich make it Θ(1).

Worst case happens wich no element of array is our target,making it T(n) = c1 * (n + 1)+ c2 * n + c3 * 1 = an + b,a linear function of n,making it Θ(n).

Average case is roughly equal to worst case,since T(n) = c2 * ((n + 1) / 2) + c2 * (n / 2) = a`n + b`,wich is Θ(n).
"""