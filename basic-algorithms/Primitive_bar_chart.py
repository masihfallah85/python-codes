#Primitive_bar_chart

"""
In this script we use '*' symbol to create a primitive bar chart proportional to element's value
"""

#Import random with wildcard import for ease(since we don't have variabel randrange) for generating random values
from random import *

#Create an empty list
lst = []

#append 10 random values to it
for i in range(10):

    lst += [randrange(1,11)]

#print the bar chart structure
print("index  value  bar_chart")

#use enumerate to safely loop through list,it also make it easier by unpacking both index and val
for index,value in  enumerate(lst):
    
    #print each index bar chart using format string
    print(f"{index:>5}  {value:>5}  {"*" * value}")