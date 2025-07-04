#change-calculator-min-coins

"""
In this script,user inputs the change cashier should give back in  cents,we should compute its value with quarters,dime,nickel and 
penny.We should use least amount of penny possible
"""

#prompt the user to input  the change
change = int(input("enter the change  cashier should give back: "))

#create variables showing number of quarters,dimes,nickels and pennies
quarters = 0
dimes = 0
nickels = 0
pennies = 0

#use while loop to find the most amount of quarters possible
while change >= 25 :
    quarters += 1
    change -= 25

#use while loop to find most amount of dimes possible
while change >= 10 :
    dimes += 1
    change -= 10

#use while loop tp find most amount of nickels possile
while change >= 5:
    nickels += 1
    change -= 5

#assign remaining money to pennies
pennies = change

#print the result
print("quarters used: ",quarters)
print("dimes used: ",dimes)
print("nickels used: ",nickels)
print("pennies used: ",pennies)