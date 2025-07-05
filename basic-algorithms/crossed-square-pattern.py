#crossed-square-pattern

"""
IN this script user inputs an integer bigger than 0 and odd.
We should createa square pattern with '#' wich is crossed and its 1/4 right side is filled
"""

#prompt user to enter edge of square
edge = int(input("enter length of edge: "))

#check if the edge is valide
if edge <= 0 or edge % 2 == 0:
    
    print("wrong edge")

else:

    #create cross lower and upper bounds for printing '#' symbol
    cross_lower_bound  = 1
    cross_upper_bound = edge - 2

#loop throw rows and columns to print square
for row in range(edge):
    
    #check if we should fill all columns
    if row == 0 or row  == edge - 1:
        
        #fill all columns
        for column in range(edge):
            
            print("#",end = " ")
        
    else:

        #print first column
        print("#",end = " ")

        for column in range(1,edge):

            #print cross lower bound
            if column == cross_lower_bound and cross_lower_bound != cross_upper_bound:
                print("#",end = " ")
            
            #fill upper bound of cross
            elif column >= cross_upper_bound:
                print("#",end = " ")

            #make blank parts empty
            else:
                print(end = "  ")
    
        #change lower and upper bound
        if cross_upper_bound > cross_lower_bound and row < (edge // 2):
            
            cross_lower_bound += 1
            cross_upper_bound -= 1
        
        else:

            cross_lower_bound -= 1
            cross_upper_bound += 1

    #make a blank line between rows
    print()