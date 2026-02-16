#Linked_deque.py


"""
In this script we implement a deque using double linked list
"""

#Importing double linked list
from Double_linked_list import doubly_linked_list

#inheritence
class linked_deque(doubly_linked_list):


    """Deque using linked list class"""

    def first(self):

        """Returns first element"""

        if self.is_empty():

            print("deque is empty")

            return

        return self._header._next._element
    
    def last(self):

        """Returns last ekemnt of deque"""

        if self.is_empty():

            print("deque is empty")

            return
        
        return self._trailer._prev._element
    
    def insert_first(self,e):


        """inserts element at the begining  of deque"""


        self._insert_between(e,self._header,self._header._next)


    def insert_last(self,e):

        """inserts element at the end of deque"""

        self._insert_between(e,self._trailer._prev,self._trailer)
   
    def delete_first(self):


        """deletes element at the begining of deque"""

        if self.is_empty():

            print("deque is empty")

            return
        
        self._delete(self._header._next)

    def delete_last(self):


        """"deletes elemnt at the end of deque"""

        if self.is_empty():

            print("deque is empty")

            return
        
        self._delete(self._trailer._prev)