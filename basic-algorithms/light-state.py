#light-state

"""
In this script we have a light bulb wich 1 indicates its turn on and 0 indicates turn off.
User give us number of states and in each line states of light bulb.
We should find how many times state of light bulb has changed.
"""

#prompt user to enter number of states
number_of_states = int(input("enter number of states: "))

#create a variable for states and prompt user to input first state
state = int(input("enter state of light bulb(1 or 0): "))

#create a  variable for previous state and assume its first state
previous_state = state

#create a variable for number of state changes and initialize it with zero
state_changes = 0

#loop through remaining states
for turn in range(number_of_states - 1):
    
    #prompt user to enter state
    state = int(input("enter state of light bulb(1 or 0): "))

    #check if state is changed
    if state != previous_state:
        previous_state = state
        state_changes += 1

#print the results
print(f"state of light bulb has changed {state_changes} time(s)")