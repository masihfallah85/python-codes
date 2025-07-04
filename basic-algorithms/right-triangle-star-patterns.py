#right-triangle-star-patterns

"""
In this script we should print 4 diffrent right triangles with ('*') wich each star is seperated by space,each triangle is seperated by
custom spaces and each line by a blank space.The overall pattern should look like this:
*        * * * * * * * * * *    * * * * * * * * * *                        * 
* *        * * * * * * * * *      * * * * * * * * *                      * * 
* * *        * * * * * * * *        * * * * * * * *                    * * * 
* * * *        * * * * * * *          * * * * * * *                  * * * * 
* * * * *        * * * * * *            * * * * * *                * * * * * 
* * * * * *        * * * * *              * * * * *              * * * * * * 
* * * * * * *        * * * *                * * * *            * * * * * * * 
* * * * * * * *        * * *                  * * *          * * * * * * * * 
* * * * * * * * *        * *                    * *        * * * * * * * * * 
* * * * * * * * * *        *                      *      * * * * * * * * * * 
"""

#use a for loop for rows
for row in range(1,11):
    
    #loop for first triangle columns : increasing stars 
    for column in range(row):
        print("*",end = " ")
    
    #seperate first triangle witth next one
    print(end = "       ")
    
    #loop for second triangle columns : decreasing stars 
    for column in range(11 - row,0,-1):
        print("*",end = " ")
    
    #seperate second triangle with next one
    print(end = "   ")
    
    #loops for third triangle columns : right aligned decreasing stars 
    for column in range(row - 1):
        print(end = "  ")

    for column in range(11 - row,0,-1):
        print("*",end = " ")
    
    #seperate third triangle with next one
    print(end = "   ")
    
    #loops for fourth triangle columns : right aligned increasing stars
    for column in range(11 - row,0,-1):
        print(end = "  ")

    for column in range(row):
        print("*",end = " ")
    
    #print the blank space between rows
    print() 