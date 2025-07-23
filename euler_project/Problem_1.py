#Problem_1

"""
Find sum of all multiples of 3 or 5 below 1000
"""
#Create a variable for sum
sum = 0

#Loop through numbers to add to sum 
for i in range(3,1000):

    #Check if i is multiple of 3 or 5
    if i % 3 == 0 or i % 5 == 0:

        sum += i

#Print the result
print("sum of multiples of 3 or 5 from 1 to 1000: ",sum)