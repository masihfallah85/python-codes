#sub-alphabet-verifier

"""
in this script,user inputs number of test cases and a refrence string for alphabets,then user inputs each test case and we should
find if it uses same sub alphabet as refrence string or not
"""

#prompt user to input number of test cases
number_of_cases = int(input("enter number of test cases: "))

#prompt user to input refrence string
refrence_string = input("enter refrence string: ")

#use the for loop to get each test case
for count in range(number_of_cases):

    #prompt user to input each case
    case = input("enter test case: ")
    
    #because we only check use of similar characters,set is ideal structure to use
    if set(case) == set(refrence_string):
        print(f"{case} has the same sub alphabet as {refrence_string} ")
    else:
        print(f"{case} doesn't have the same sub alphabet as {refrence_string}")