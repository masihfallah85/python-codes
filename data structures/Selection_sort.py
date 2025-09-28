#Selection_sort

"""
In this script we implement selection sort,each time from i = 1 to n we find minimum of A[i : n] and swamp it with A[i].
When the function terminates(ie i = n) each subarray A[i:n] have minimum element of itself in A[i],sorting correctly.
In floyde_hoare logic:
{j = i + 1}j = for every i A[j] < A[i]{A[i] = A[j] and i = i + 1} / [i = 1]find minimum of A[i:n]{A[1 : n] is sorted}
"""

def selection_sort(array):

    """This functions sorts and iterablee object using selection sort"""

    for i in range(len(array)): # cost = c1 times = n

        minimum = i # cost = c2 tims = n - 1

        for j in range(i + 1,len(array)): # cost = c3 times = sum of  ti form 1 to n-1

            if array[j] < array[i]: # cost = c4 times = sum of (ti -  1) from 1 to n-1

                minimum = j  #cost = c5 times = xi

        array[i] = array[minimum] # cost = c6 times = n - 1


    return array

#Create an example array
lst = [4,6,7,9,8,3,2,1,10]

#Printing result
print(selection_sort(lst))

"""
Best case happens if array is already sorted,so xi = 0.and eahc ti always runs n - i times
T(n) = c1 * n + c2 *(n - 1) + c3 * (sum of (n - i) from 1 to  n) + c4 * (sum of (n-i-1)from 1 to n) + c5 * 0 + c6 * (n - 1) =
c1 * n + c2 * (n - 1) + c3 * (n * (n - 1) / 2) +  c4 * (n * (n - 3) / 2) + c6 * (n - 1) = an**2 + bn + c a quadradic function of n 
meaning complexity of it becomes Θ(n**2)

Wosrt case happens when array is reverse sorted,so xi = sum of (ti - 1 from 1 to n),this adds c5 * (n * (n - 3) / 2) to best case
T(n) ,again the complexity becomes Θ(n**2)

Average case happens when minimum = j happens half of subarray,adding a c5 * (n * (n - 3) / 4) to best case T(n),again having 
complexity of Θ(n**2)
"""