#Count_differnces.py

# for input/output
import sys
read_all = sys.stdin.read
write = sys.stdout.write

def merge_count(arr, left, middle, right):

    """counts misplacments while emrging two arrays"""

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

    total = 0

    while i < n and j < n_1:

        if arr_1[i] <= arr_2[j]:

            arr[k] = arr_1[i]

            i += 1
        else:

            arr[k] = arr_2[j]

            j += 1

            total += (n - i)

        k += 1

    while i < n:

        arr[k] = arr_1[i]
  
        i += 1

        k += 1

    while j < n_1:

        arr[k] = arr_2[j]

        j += 1

        k += 1

    return total

def merge_sort_count(arr, left, right):
    

    """count misplacment instead of sorting via merge sort"""

    total= 0

    if left < right:

        middle = (left + right) // 2

        total += merge_sort_count(arr, left, middle)

        total += merge_sort_count(arr, middle + 1, right)

        total += merge_count(arr, left, middle, right)

    return total

data = read_all().split()
n = int(data[0])
lst = list(map(int, data[1:]))

left = 0
right = len(lst) - 1

result = merge_sort_count(lst, left, right)

write(str(result))
write('\n')