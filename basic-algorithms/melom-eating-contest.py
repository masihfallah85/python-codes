#melom-eating-contest

"""
In this script, we simulate a melon-eating contest with n melons (1 to 100).
Each melon has an index and a mass (integer).
Each time, the two melons with the smallest indices are compared, and the one with lesser mass is eaten.
This continues until only one melon remains.
The goal is to output the index of the final remaining melon — the one with the greatest mass.
Constraints: No functions or data structures are used.
"""

#prompt user to enter number of melons
number_of_melons = int(input("enter number of melons: "))

#prompt user to enter first melon's mass
current_melon = int(input("enter mass of melon:  "))

#create a variable for remaining weight and initialize it to first melon's mass
remaining_melon_mass = current_melon

#create a variable for remaining index and storing indexes and intitialize them to 1
remaining_index = 1
index = 1

#loop through other melons to find the remaining melon
for count in range(number_of_melons - 1):
    
    #prompt user to enter next melon's mass
    current_melon = int(input("enter melons mass: "))
    
    #increase index to current melon's index
    index += 1

    #compare mass of it with remaining melon,if it has bigger mass then  make the current melon remaining one
    if current_melon > remaining_melon_mass:
        remaining_melon_mass = current_melon 
        remaining_index = index

#print the result
print("remaining melon's index: ",remaining_index)