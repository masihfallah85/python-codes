#dice-simulation.py

"""
In this script we see frequency of each face of dice if we roll it n times
"""

#import random module for random face
import random

#prompt user to input number of rolls
roll = int(input("Enter number of rolls: "))

#create six variables for frequency of faces
frequency_face_1 = 0

frequency_face_2 = 0

frequency_face_3 = 0

frequency_face_4 = 0

frequency_face_5 = 0

frequency_face_6 = 0

#loop through number of rolls to count frequency of each face
for i in range(roll):

    #create a variable to store a random number from 1 to 6 representing a face
    face = random.randrange(1,7)

    #check wich face to add to it's frequency
    if face == 1:
        
        frequency_face_1 += 1
    
    elif face == 2:

        frequency_face_2 += 1

    elif face == 3:

        frequency_face_3 += 1

    elif face == 4:

        frequency_face_4 += 1

    elif face == 5:

        frequency_face_5 += 1
    
    elif face == 6:

        frequency_face_6 += 1

#print results
print("face   frequency")

print(f"{1:>4}{frequency_face_1:>12}")

print(f"{2:>4}{frequency_face_2:>12}")

print(f"{3:>4}{frequency_face_3:>12}")

print(f"{4:>4}{frequency_face_4:>12}")

print(f"{5:>4}{frequency_face_5:>12}")

print(f"{6:>4}{frequency_face_6:>12}")