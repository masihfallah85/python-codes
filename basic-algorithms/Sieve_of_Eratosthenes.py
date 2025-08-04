#Sieve_of_Eratosthenes.py

"""
In this script we want to find all prime numebrs below 1000 using Sieve of Eratosthenes algorithm
"""

#Create a list assuming indexes 0 and 1 are false and other are true
lst = [False,False] + [True] * 998

#Loop through indexes
for i in range(0,1000):

    #Check if value at that index is true
    if lst[i] == True :

        #Loop through index multipliers to make them false
        for num in range (i ** 2,1000,i):

            lst[num] = False

#Print the result
print("prime numbers below 1000")

for i in range(0,1000):

    if lst[i] == True:

        print(f"{i:>24}")