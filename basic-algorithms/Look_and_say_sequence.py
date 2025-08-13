#Look_and_say_sequence.py

"""
In this script we should find nth term of look and say sequence: 1,11,21,1221......
"""

def look_and_say(n):

    """This function find nth term of look and say sequence"""

    if n == 1:

        return "1"
    
    else:

        prev_sequence = look_and_say(n - 1)

        count = 1

        new_sequence = ""

        for i in range(1,len(prev_sequence)):

            if prev_sequence[i] == prev_sequence[i - 1]:

                count += 1

            else:

                new_sequence += str(count) + prev_sequence[i - 1]

                count = 1
        
        new_sequence += str(count) + str(prev_sequence[-1])

        return new_sequence
    
#Prompt user to enter nth term of sequence
term = int(input("Enter nth term of sequence: "))

#Print the result
print(f"{term}th term of the sequence is {look_and_say(term)}")