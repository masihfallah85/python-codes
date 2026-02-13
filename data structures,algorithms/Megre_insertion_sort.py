#Megre_insertion_sort.py

def insertion_sort(arr,left,right): 

    """insertion sort function"""

    for i in range(left + 1, right + 1):

        key = arr[i]

        j = i - 1

        while j >= left and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

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


def merge_sort(arr,left,right,k):

    """This function sorts an array with merge sort"""

    middle = (left + right) // 2

    if left < right:
        if (right - left + 1) <= k:

            insertion_sort(arr,left,right)

        else:

            merge_sort(arr,left,middle,k)

            merge_sort(arr,middle + 1,right,k)

            merge(arr,left,middle,right)


lst = []

n = int(input())

k = int(input())

for i in range(n):

    lst.append(int(input()))


left = 0

right = len(lst) - 1

merge_sort(lst,left,right,k)

for i in range(len(lst)):

    print(lst[i],end = " ")