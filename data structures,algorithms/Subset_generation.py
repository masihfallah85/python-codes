#Subset_generation.py


"""
In this script we generate subsets of a set non recusivly using stack and queue
"""

class Empty(Exception):

    """Error for attempting to access empty container"""

    pass

class Stack:

    """This class implements a stack with python list data type"""

    def __init__(self):

        """Constructor"""

        self._array = []
    
    def __len__(self):

        """This function retruns number of element"""

        return len(self._array)
    
    def isempty(self):

        """This function verifies if stack is empty or not"""

        return len(self._array) == 0
    
    def push(self,element):

        """This function adds an element to stack"""

        self._array.append(element)


    def top(self):

        """This function shows last added element of stack"""


        if self.isempty():

            raise Empty("Stack is empty")
        
        else:

            return self._array[-1]
    
    def pop(self):


        """This function removes last element added to stack"""

        if self.isempty():

            raise Empty("stack is empty")
        
        else:

            self._array.pop()

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

def genrate_subsets(target_set : set):

    """This functions generates subsets of a set"""

    stack = Stack()

    queue = Queue()

    empty_set = set()

    queue.enqueue(empty_set)

    for i in target_set:

        stack.push(i)


    while(not stack.isempty()):

        element = stack.top()

        for i in range(len(queue)):

            set_a = queue.dequeue()

            queue.enqueue(set_a)

            queue.enqueue(set_a | {element})
    
        stack.pop()

    while not queue.isempty():
        
        print(queue.dequeue(), end=" ")


#Testing algorithm
if __name__ == "__main__"  :

    s = {1,2,3}

    genrate_subsets(s)