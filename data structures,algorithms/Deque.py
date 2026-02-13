#Deque.py

"""
In this script we implement a deque
"""

class Empty(Exception):
    
    """Error for attempting to access empty container"""
    pass


class Deque:
    
    """Deque class with array"""

    capacity = 2

    def __init__(self):
        
        """Constructor"""

        self._array = [None] * Deque.capacity

        self._size = 0

        self._front = 0

    def __len__(self) -> int:
        
        return self._size

    def isempty(self) -> bool:
        
        return self._size == 0

    def first(self):
        
        """Returns front of deque"""

        if self.isempty():
            
            raise Empty("deque doesnt have any elements")
        
        return self._array[self._front]

    def last(self):
        
        """Returns last element of deque"""

        if self.isempty():
            
            raise Empty("deque doesnt have any elements")
        
        last_index = (self._front + self._size - 1) % len(self._array)

        return self._array[last_index]

    def _resize(self, cap):
        
        """Resize the deque when full"""

        old_array = self._array

        self._array = [None] * cap

        index = self._front

        for i in range(self._size):
            
            self._array[i] = old_array[index]

            index = (index + 1) % len(old_array)

        self._front = 0

    def add_last(self, element):
        
        """Adds element to the back"""

        if self._size == len(self._array):
            
            self._resize(2 * len(self._array))

        place = (self._front + self._size) % len(self._array)
        
        self._array[place] = element

        self._size += 1

    def add_first(self, element):
        
        """Adds element to the front"""

        if self._size == len(self._array):
            
            self._resize(2 * len(self._array))

        self._front = (self._front - 1) % len(self._array)

        self._array[self._front] = element

        self._size += 1

    def delete_first(self):
        
        """Removes and returns front element"""

        if self.isempty():
            
            raise Empty("deque is empty")

        temp = self._array[self._front]

        self._array[self._front] = None

        self._front = (self._front + 1) % len(self._array)

        self._size -= 1

        return temp

    def delete_last(self):
        
        """Removes and returns last element"""

        if self.isempty():
            
            raise Empty("deque is empty")

        last_index = (self._front + self._size - 1) % len(self._array)

        temp = self._array[last_index]

        self._array[last_index] = None

        self._size -= 1

        return temp