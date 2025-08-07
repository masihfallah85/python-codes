#Word_count.py 

"""
In this script we tokenize a text and count it's words.
"""

#Create a variable for text
text = ("This is a sample string  with some words "
        "This is a another sample string with minor diffrences.")

#Create variables for total number of unique words
unique_words = 0

#Create a dictionary for placing unique words ad their count in it
words = {}

#Loop through texts to count words
for character in text.split():

    if character in words:

        words[character] += 1

    else:

        words[character] = 1

        unique_words += 1

#Print the result
print(f"{"Word":<12}Count")

for i,j in words.items():

    print(f"{i:<12}{j}")

print(f"Number of unique words : {unique_words}")