#Problem_2

"""
Find sum of even valued numbers of fibonacci sequence that do not exceed four milion
"""

#Create variables for first two terms
term_1 = 1

term_2 = 2

#Create a variable to store sum of terms
total = 2

#Loop through sequence's numbers
while term_2 <= 4_000_000:

    term_1 , term_2 = term_2 , term_1 + term_2

    if term_2 % 2 == 0:

        total += term_2

#Print the result
print("Sum of even valued fibonacci numbers that do not exceed 4 milion: ",total)
