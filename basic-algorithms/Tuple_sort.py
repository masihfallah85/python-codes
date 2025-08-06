#Tuple_sort.py

"""
In this script we have some tuples we sumerize by mapping them by description and price then sorting them based on price
"""

#Import itemgetter from operator library to sort based on price index
from operator import itemgetter

#Create a list containing tuples(part number,description,quantity,price)
lst = [(83,"Electric sander",7,57.98),(24,"Power saw",18,99.9),(7,"Sledge hammer",17,21.5),(77,"Hammer",76,11.99),(39,"Jig saw",3,79.5)]

#Map the list to a summarized lsit containg description and item description and quantity
summarized_lst  = list(map(lambda x : (x[1],x[3]),lst))

#Sort summarized list based on price
sorted_summarized_lst = sorted(summarized_lst,key = itemgetter(1)) 

#Print the resulted list
for i in sorted_summarized_lst:

    print(i,end = " ")