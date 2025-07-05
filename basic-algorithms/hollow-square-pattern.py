#hollow-square-pattern

"""
In this script user enters two square's edges,one bigger and one smaller.
We should verify if bigger square is actually bigger,then printing a hollow square with # symbol,which bigger edge is bigger
square's edge and smaller edge is smaller square's edge.
for example the pattern for 7 and 3:
* * * * * * *
* * * * * * *
* *       * *
* *       * *
* *       * *
* * * * * * *
* * * * * * *
"""

#prompt user to input bigger square's edge
bigger_edge = int(input("enter bigger square's edge: "))

#prompt user to input smaller square's edge
smaller_edge = int(input("enter smaller square's edge: "))

#validate inputs
if bigger_edge <= smaller_edge :
    
    print("wrong edges")

#if square can't be centered properly
elif bigger_edge % 2 != smaller_edge % 2:
     
     print("wrong edges")

else:
    #calculate inner hollow square's bounds within outer square
    row_lower_bound = (bigger_edge - smaller_edge) // 2
    row_upper_bound =  bigger_edge - row_lower_bound - 1
    column_lower_bound = row_lower_bound
    column_upper_bound = row_upper_bound

    #loop through rows of square
    for row in range(bigger_edge):

        #loop throgh columns
        for column in range(bigger_edge):

            #check if row and column fits inside hollow part,else print # symbol
            if (row_lower_bound <= row <= row_upper_bound) and (column_lower_bound <= column <= column_upper_bound):
                
                print( end = "  ")

            else:
                print("#",end = " ")

        #print blank line after each row
        print()
