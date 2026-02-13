#Parentheses.py

"""
In this script we implement a valid parentheses check with stack
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

            temp = self._array[-1]

            self._array.pop()

            return temp

def match(string : str) -> bool:

    left = "("

    right = ")"

    s = Stack()

    for c in string:

        if c == left:

            s.push(c)

        elif c == right:

            if s.isempty():

                return False
            
    return s.isempty()