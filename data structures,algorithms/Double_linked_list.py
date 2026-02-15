#Double_linked_list.py


"""
In this script we implement a double linked list,linked list wich each node is connected to previous and next node
"""

class node:

    """Node class for single node"""

    #For memmory efficency
    __slots__ = "_element" , "_prev" , "_next"

    def __init__(self,element,prev,next):

        self._element = element

        self._prev = prev

        self._next = next

    
class doubly_linked_list:

    """Double linked list class"""

    def __init__(self):

        self._header = node(None,None,None)

        self._trailer = node(None,None,None)

        self._header._next = self._trailer

        self._trailer._prev = self._header

        self._size = 0

    def __len__(self):

        """Returns length of list"""

        return self._size
    

    def is_empty(self):

        """Checks if list is empty or not"""

        return 0 == self._size
    
    def _insert_between(self,element,predecessor : node,succesor : node) -> node:

        """Adds an element between two node"""

        new_node = node(element,predecessor,succesor)

        predecessor._next = new_node

        succesor._prev = new_node

        self._size += 1

        return new_node
    
    def _delete(self,element : node):

        """Deletes an element"""

        predecessor = element._prev

        succesor = element._next

        predecessor._next = succesor

        succesor._prev = predecessor

        self._size -= 1

        data = element._element

        element._next = element._prev = element._element = None

        return data