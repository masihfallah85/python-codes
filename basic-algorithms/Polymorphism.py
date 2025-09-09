#Polymorphism.py

"""
In this script we implement a simple polymorphism code.
"""

class polygon:

    def __init__(self,sides,points):

        self.sides = sides

        self.points = points

        if points != sides:

            raise ValueError("Number of sides doesn't match point")
    
class triangle:

    def __init__(self,sides,points):

        polygon(sides,points)

        if sides != 3:

            raise ValueError("Number of sides is incorrect")
        
        if points != 3:

            raise ValueError("Number of points is incorrect")
        
        def __str__(self):

            return "triangle"
        
        def __repr__(self):

            return "triangle"
        

class square:

    def __init__(self,sides,points):

        polygon(sides,points)

        if sides != 4:

            raise ValueError("Number of sides is incorrect")
        
        if points != 4:

            raise ValueError("Number of points is incorrect")
        
        def __str__(self):

            return "square"
        
        def __repr__(self):

            return "square"
        
class polygon_collection:

    def __init__(self):

        self.triangle = []

        self.square = []

    def add(self,polygon):

        if polygon.sides == 3:

            self.triangle.append(polygon)

        elif polygon.sides == 4:

            self.square.append(polygon)