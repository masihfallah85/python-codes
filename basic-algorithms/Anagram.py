#Anagram.py

"""
In this script we genrate all permutations of a given stirng
"""

def permute(string):

    """This function genrates all permutations of a given string as a list"""

    if len(string) == 1:

        return [string]
    
    else:

        result = []

        for i in range(len(string)):

            fixed_char = string[i]

            remaining = string[:i] + string[i + 1:]
            
            for sub_permutation in permute(remaining):

                result.append(fixed_char + sub_permutation)

    return result

#Prompt user to input a string
string = input("Enter a string: ")

#Create a list to store all permutations
lst = permute(string)

#Print the result
print(f"Permutations of {string}: ", end = "")

for i in lst:

    print(i,end = " ")