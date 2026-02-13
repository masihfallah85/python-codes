#Queue.py

"""
In this script we implement a Queue data structure
"""

class Empty(Exception):

    """Error for attempting to access empty container"""

    pass


class Queue:


    """Queue class with array"""


    def __init__(self):

        """Constructor"""

        self._array  = [None] * 2

        self._size = 0

        self._front = 0


    def __len__(self) -> int:

        """This functions retuns size of queue"""

        return self._size
    
    def isempty(self) -> bool:
        
        """This function checks if queue is empty or not"""

        if self._size == 0:

            return True
        
        else:

            return False
        
    def first(self):

        """This functions returns front of queue"""

        if self.isempty():

            raise Empty("Queue doesn't have any elements")
        
        else:

            return self._array[self._front]
        

    def dequeue(self):

        """This functions removes and returns front element of  queue"""

        temp = self._array[self._front]

        self._array[self._front] = None

        self._front = (self._front + 1) % (len(self._array))

        self._size -= 1


        return temp
    
    def _resize(self,cap):


        """This functions resizes queue when full each time we add an element"""

        old_array = self._array

        self._array = [None] * cap

        iteration = self._front

        for i in range(self._size):

            self._array[i] = old_array[iteration]

            iteration = (iteration + 1) % len(old_array)

        self._front = 0

    def enqueue(self,element):

        """This functions adds an element to queue"""

        if self._size == len(self._array):

            self._resize(2 * len(self._array))

        place = (self._front + self._size) % len(self._array)


        self._array[place] = element

        self._size += 1