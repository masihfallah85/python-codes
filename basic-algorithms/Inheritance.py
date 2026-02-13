#Inheritance.py


"""
In this script we implement a simple series of progression classes using inheritance
"""

class progression:


    """General progression class"""

    def __init__(self,start = 0):

        """Constructor"""

        self._current = start
    
    def _advance(self):

        """This function advances in sequence,it changes acording to type of progression"""

        self._current += 1

    def __next__(self):

        """This function is iterator to move to next elemnt if it exist"""

        if self._current is None:

            raise StopIteration()
        
        else:
        
            answer = self._current

            self._advance()

            return answer
        
    def __iter__(self):

        """Iter method of iterator"""

        return self
    
    def print_progression(self,n):


        """This function prints next n elements"""


        print(" ".join(str(next(self)) for j in range(n)))


class   Arithmetic_Progression(progression):

    """Arithmetic progression,progress by addinga constant each time"""  

    def __init__(self,increment = 1,start = 0):

        """Constructor"""

        super().__init__(start)

        self._increment = increment

    def _advance(self):

        """Each time advances by adding a constant"""

        self._current += self._increment

class Geometric_progression(progression):

    """Geomtetric progression,progress by multiplying by a constant"""

    def __init__(self,base = 2,start = 1):

        """Constructor"""

        super().__init__(start)

        self._base = base


    def _advance(self):

        """Advance by multiplying by a constant"""

        self._current *= self._base


#testing classes
if __name__ == "__main__" :

    print("Arithmetic progression")

    arithmetic = Arithmetic_Progression(2,2)

    arithmetic.print_progression(10)

    print("Geometric progression")

    geometric = Geometric_progression(3,1)

    geometric.print_progression(10)


    

