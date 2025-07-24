#Keyboard_cursor.py

"""
In this script we should simulate left and right insertion of text with letters R and L like a cursor.
We can use left and right stack for this.
"""

#Prompt user to input the text
text = input("Enter the text: ")

#Create left and right stack
left_stack = []

right_stack = []

#Create a variable for final text
final_text = ""

#Loop through words of text for inserting them in stacks
for i in text:
    
    #check if text goes out of bound
    if (i == "L" and len(right_stack) == 0) or (i == "R" and len(left_stack) == 0):

        print("Text goes out of bound")

        break
    
    #else insert them in right and left stacks 
    elif i == "R":

        right_stack.append(left_stack[-1])

        left_stack.pop()
    
    elif i == "L" :

        left_stack.append(right_stack[-1])

        right_stack.pop()
    
    else:

        right_stack.append(i)

else:

    #Reverse left stack for accurate representation
    left_stack.reverse()

    #Add left stack to right stack
    right_stack.extend(left_stack)

    #Add letters of right stack to final text
    for word in right_stack:

        final_text += word
    
    #Print the output
    print(final_text)