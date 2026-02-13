#Heap_sort.py


"""
In this script we implement a heap sort,wich is used for a method of sorting called heap sort,with complexity of O(nlgn) and property of being inplace.
"""

def max_heapify(arr, heap_size, i):

    """
     This fucntion induces a heap property inside the array,by fixing it for eahc subtree with root as i.
    """

    largest = i

    left = 2*i + 1

    right = 2*i + 2

    if left < heap_size and arr[left] > arr[largest]:

        largest = left

    if right < heap_size and arr[right] > arr[largest]:

        largest = right

    if largest != i:

        arr[i] , arr[largest] = arr[largest] , arr[i]

        max_heapify(arr, heap_size, largest)


def heap_sort(arr):

    """
    Heap sort fucntion,max heapify the array,eahc time swap last and root of tree and heapify the prefix
    """


    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):


        max_heapify(arr, n, i)

    for end in range(n - 1, 0, -1):

        arr[0] , arr[end] = arr[end] , arr[0]  

        max_heapify(arr, end, 0)            

    return arr
