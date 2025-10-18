#Merge_sort.py

"""
In this script we want to implement merge sort,with compelxity of O(nlg(n)).in floyde hoar logic we can write it as this:
∀A,l,r{0≤l≤r<∣A∣} MergeSort(A,l,r) {sorted(A[l..r])∧perm(A[l..r],A0​[l..r])}.
"""

def merge(arr, left, middle, right):
    

    """This fucntion merges two arrays in ascending order"""

    n = middle - left + 1

    n_1 = right - middle

    arr_1 = [0] * n

    arr_2 = [0] * n_1

    for i in range(n):

        arr_1[i] = arr[left + i]

    for j in range(n_1):

        arr_2[j] = arr[middle + 1 + j]

    i = j = 0

    k = left

    while i < n and j < n_1:

        if arr_1[i] <= arr_2[j]:

            arr[k] = arr_1[i] 

            i += 1
        else:

            arr[k] = arr_2[j]  

            j += 1

        k += 1

    while i < n:

        arr[k] = arr_1[i]

        i += 1

        k += 1

    while j < n_1:

        arr[k] = arr_2[j]

        j += 1

        k += 1

def merge_sort(arr, left, right):

    """This function sorts an array by merge sort"""

    if left < right:

        middle = (left + right) // 2

        merge_sort(arr, left, middle)

        merge_sort(arr, middle + 1, right)

        merge(arr, left, middle, right)

lst = [5, 7, 6, 8, 9, 3, 4]

merge_sort(lst, 0, len(lst) - 1)

print(lst)
