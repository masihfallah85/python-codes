#Summing_array

"""
In this script we implement summing elements of an array algorithm.since at first sum of elemtns is zero wich is correct,and in eahc step assuming we summed subarray A[1:i-1]
and when we add A[i] to it we summ elemtns of A[1:i].after the loop goes out of bound(ie n + 1) and terminates the previous A[1:n] wich is sum of all elements of array.
in floyde_hoare logic we can express it as this:
{sum = sum of elements of A[1:i - 1]}adding A[i] to sum{sum = sum of elements of A[1:i]} / {sum = 0}adding A[i] to sum{sum = elements of A[1:n]}
"""

def total(array):

    "This function sumes the elements of an iterable object"

    total = 0 #cost = c1 times = 1

    for i in array: #cost = c2 times = n + 1

        total += 1 #cost = c3 times = n 

    return total

#Creating an example array

lst = [1,2,3,4,5,6,7,8,9,10]

print(total(lst))

"""
In this algorithm worst,best and average case are similar.

T(n)  = c1 * 1 + c2 * (n + 1) + c3 * (n) = an + b.

it's a linear function of n,the complexity of it is Θ(n).
"""