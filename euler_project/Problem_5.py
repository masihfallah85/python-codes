#Problem_5.py

"""
What's the first number wich is  multiply of 1 to 20(assume first number wich is multiply of 1 to 10 is 2520)
"""

#Creating an upper limit by  multipling 2 to 20
upper_bound = 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20

#Create a variable for answer 
answer = 0

#Loop throgh 2520 to upper limit to find answe
for i in range(2520,upper_bound + 1):

    #Check divisibility
    if  i % 20 == 0 and i % 19 == 0 and i % 18 == 0 and i % 17 == 0 and i % 16 == 0 and i % 14 == 0 and i % 13 == 0 and i % 11 == 0:

        answer = i

        break

#Print the answer
print(f"{answer} is the first number divisible by 1 to 20")