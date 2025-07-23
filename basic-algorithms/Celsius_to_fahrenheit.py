#Celsius_to_fahrenheit.py

"""
In this script,we turn celsius degrees from 1 to n to fahrenheit degrees and show them in tabular form.
"""

#Defining a function wich changes celsius to fahrenheit
def convert(celsius):

    fahrenheit = (9 / 5) * celsius + 32

    return fahrenheit

#Prompt user to input a celsius degree bigger than 1
celsius = int(input("Enter a celsius degree bigger than 1: "))

#Check if user entered correct number
if celsius <= 1:

    print("invalid degree")

else:

    #Create tabel's layout
    print("Celsius  Fahrenheit")

    #Loop through degrees to print them
    for i in range(1,celsius):
        
        #round fahrenheit degree to 2 digits using built in round function
        print(f"{i:>7}  {round(convert(i),2):>10}")