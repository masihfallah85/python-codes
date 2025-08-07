#Problem_14.py

"""
In collatz problem,wich number under 1_000_000 produces longest sequence of numbers?
"""

#Create a dictionary to store length of each term
collatz = {}

def collatze_catch(n):

    """This function find length of each term's length"""

    if n in collatz:

        return collatz[n]
    
    if n == 1:

        collatz[n] = 1

    elif n % 2 == 0:

        collatz[n] = 1 + collatze_catch(n // 2)

    elif n % 2 == 1:

        collatz[n] = 1 + collatze_catch(3 * n + 1)

    return collatz[n]

#Create a variable to store length 
length = 0

#Create variables for maximum term and lengthes
maximum_term = 0

maximum_lengthes = 0

for i in range(1,1_000_001):

    length = collatze_catch(i)

    if maximum_lengthes < length:

        maximum_lengthes = length

        maximum_term  = i

#Print the result
print(f"{maximum_term} produces largest sequence")