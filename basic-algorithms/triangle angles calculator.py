#triangle angles calculator

"""in this program we are given 3 numbers,after validating if they can make a triangle,we should find all three angles of it"""

#for arccosin of angles(for law of cosins) we should use built-in math module
import math

#get edges from user
edge_1 = int(input("enter first edge: "))
edge_2 = int(input("enter second edge: "))
edge_3 = int(input("enter third edge: "))

#confirm if you can make a triangle or not
if edge_1 + edge_2 <= edge_3 or edge_2 + edge_3 <= edge_1 or edge_3 + edge_1 <= edge_2:
    print("the edges are invalid for a triangle")

else:
#we compute cosin of each edge by algebraicly manipulate formula c**2 = a**2 + b**2 - 2abcosin (law of cosins)
    cosin_angle_1 = ((edge_2**2 + edge_1**2)-edge_3**2)/(2 * edge_1 * edge_2)
    cosin_angle_2 = ((edge_3**2 + edge_1**2)-edge_2**2)/(2 * edge_1 * edge_3)
    cosin_angle_3 = ((edge_2**2 + edge_3**2)-edge_1**2)/(2 * edge_3 * edge_2)

#we use python built in acos() fucntion to revert them back to radian
    angle_1_rad = math.acos(cosin_angle_1)
    angle_2_rad = math.acos(cosin_angle_2)
    angle_3_rad = math.acos(cosin_angle_3)

#we revert angles from radian to degree form
    angle_1 = math.degrees(angle_1_rad)
    angle_2 = math.degrees(angle_2_rad)
    angle_3 = math.degrees(angle_3_rad)

#showing the output
    print("first angle:",angle_1,"second angle:",angle_2,"third angle",angle_3)