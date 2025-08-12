#Largest_substring.py

"""
In this script we have a list of words and a stirng,we should find largest word wich is substring of the string.
"""

def is_substring(word,string):

    """This function checks if a word is substring of a string """

    index = 0

    substring = False

    for i in range(len(word)):

        for j in range(index,len(string)):

            if word[i] == string[j]:

                index = j + 1

                substring = True
        
        if substring == False:

            return substring

    return substring

#Create a variable for maximum length and substring
max_length = 0

max_substring = ""

#Prompt user to enter a list of words
lst = input("Enter list of words: ").split()

#Prompt user to enter  a string
string =  input("Enter a string: ")

#Loop through list to find maximum substring
for i in lst:

    if is_substring(i,string) and len(i) > max_length:

        max_length = len(i)

        max_substring = i

#Print the result
print(f"{max_substring.title()} is substring of {string} with maximum lenght of {max_length}")