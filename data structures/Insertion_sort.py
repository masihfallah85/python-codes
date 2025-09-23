#Insertion_sort.py

"""
In this script we implement insertion sort algorithm and analyze it's complexity,by loop invariant we can prove its correct

1.initialy i = 2 so A[1:i-1] is a single object,sorted

2.inductivly assume the A[1:i-1] is sorted,by the method in isnertio nsort,the sub_array by adding A[i] ie A[1:i] become sorted too

3.after the loop goes out of bound(ie i = n + 1),the entire subarray of previous step wich is whole array now is sorted

in floyde-hoare logic if {p}c{Q} wich p is initial conditon,c is command sand Q is what si achived after command:

{A[1:i-1] is sorted and i <= n}insert A[i] to A[1:i-1] {A[1:i] is sorted} / {A[1:i-1] = A[1] is sorted}for i 2 to n insert A[i]{A[1:n] is sorted}

Wich top triple  is logic isndie the loop and bottom triple is logic outside the loop prespective.
"""


def insertion_sort(arg): 

    """This function sorts an iterable object by insertion sort method,from second object to last one,each time we fix it's place amoung previous objects"""

    for i in range(1,len(arg)): # cost = c1 times = n

        #Creating the key we want to sort

        key = arg[i] #cost = c2 times = n - 1

        #Initializing the index befor the key
        
        j = i - 1 # cost = c3 times = n - 1

        #Looping through previous objects fixing their position

        while j >= 0 and arg[j] > key: #cost = c4 times = sum of ti from 1 to n-1

            arg[j + 1] = arg[j]  #cost = c5 times = sum of (ti - 1) from 1 to  n-1

            j -= 1   #cost = c6 times = sum of of (ti - 1) from 1 to n-1

        #fixing the key positon

        arg[j + 1] = key #cost = c7 times = n - 1

    return arg

#total cost  => T(n) = c1 * n + c2 * (n - 1) + c3 * n-1 + c4 * sum of (ti) from 1 to n-1 + c5 * sum of (ti - 1) from 1 to n-1 + c6 * sum of (ti - 1) from 1 to n-1 + c7 * (n -1)

#Creating an example list
lst = [4,6,5,8,7,9,3,1,2]

#Printing the result
print(insertion_sort(lst))

"""
Best case accures when all  array is sorted,so the while loop exit on the conditon so ti = 1 therefor:

T(n) =  c1 * n + c2 * (n - 1) + c3 * n-1 + c4 * sum of (1) from 1 to n-1 + c5 * sum of (1 - 1) from 1 to n-1 + c6 * sum of (1 - 1) from 1 to n-1 + c7 * (n -1) =

c1 * n + c2 * (n - 1) + c3 * (n - 1) + c4 * (n - 1) + c7 * (n - 1) = an + b , a linear function of n,if we ignore a and b for statment cost we reach to complexity 
 
of  Θ(n).

Worst case accures when all array is reverse sorted,so in each while loop ti happens i + 1 times,therefor:

T(n) =  c1 * n + c2 * (n - 1) + c3 * n-1 + c4 * sum of (i + 1) from 1 to n-1 + c5 * sum of (i) from 1 to n-1 + c6 * sum of (1 - 1) from 1 to n-1 + c7 * (n -1) =

c1 * n + c2 * (n - 1) + c3 * (n - 1) + c4 * (n)(n + 1 1) / 2 + c5 * (n) * (n -1) / 2 + c6 * (n) * (n - 1) / 2 + c7 * ( n - 1) = a * n**2 + b * n + c

a quadratic function of n,if we ignore a,b,c statement costs and n since the rate fo gowth for doesn't depend on it(for large n it's insignificant) we reach to 

compelxity of Θ(n**2)

Average case is roughly equal to worst case

"""