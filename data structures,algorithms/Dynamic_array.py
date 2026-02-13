#Dynamic_array.py


"""In this script we implement a Dynamic array data structure"""

#Ctypes for low-level array
import ctypes

class Dynamic_array:

    def __init__(self):

        """Constructor"""

        self._n = 0

        self._capacity = 1

        self._array = self._make_array(self._capacity)

    def _make_array(self,capacity):

        """Create an array with fixed capacity"""

        return (capacity * ctypes.py_object)()
    

    def __len__(self):

        """This function returns length of array"""

        return self._n
    
    def __getitem__(self,k):

        """Return kth index"""

        if not 0 <= k < self._n:

            raise IndexError("Invalid index")
        
        else:

            return self._array[k]
    
    def _resize(self,capacity):

        """Resize array to hold more item"""

        temp_array = self._make_array(capacity)

        for i in range(self._n):

            temp_array[i] = self._array[i]


        self._array = temp_array

        self._capacity = capacity


    def append(self,obj):

        """Add an element to array"""

        if self._n == self._capacity:

            self._resize(2 * self._capacity)

        self._array[self._n] = obj

        self._n += 1


    def print_element(self,k):

        """Print kth element"""

        print(self.__getitem__(self,k))

if __name__ == "__main__" :

    array = Dynamic_array()

    for i in range(2,12):

        array.append(2 * i)

    for i in range(len(array)):

        print(array[i],end = " ")


"""
Amortized complexity:

for eahc time we dont reach the 2 ^ ith index  ,we have O(1) complexity,and each time we reach 2 ^ ith index we have O(n) 

complexity do to copy,here we assume we have k times O(1) complexity and one o(k) compelxity we add them to ghter to have 2k ,devided

by k we have average complexity of O(2) wich is O(1)
"""