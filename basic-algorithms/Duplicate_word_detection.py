#Duplicate_word_detection.py

"""
In this script we use a counter to detect duplicate words in a sentece without case sensetivity.
"""

#Import counter from collections library
from collections import Counter

#Prompt user to input a sentece
sentence = input("Enter a sentece: ")

#Create a counter containing lower case form of tokenized sentece
counter = Counter((sentence.lower()).split())

#Loop through counter to print the result
for word,count in counter.items():

    if count > 1:

        print(f"{word:<12}{count}")