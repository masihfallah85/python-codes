#Problem_17

"""
How many letters are used for writing numbers from 1 to 1000?
"""

def count_length_letters(n):


    """This function counts length of letters of 1 to n up to n = 1000"""

    if n > 1000:

        return ValueError("Number exceeds 1000")
    
    total_length = 0

    ones = {1 : "one",2 : "two",3 : "three",4 : "four",5 : "five",6 : "six",7 : "seven",8 : "eight",9 : "nine",0 : ""}   

    teens = {10: "ten" ,11 : "eleven",12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen" , 17 : "seventeen", 18 : "eighteen", 19 : "nineteen"} 

    tens = { 2 : "twenty",3 : "thirty" , 4 : "forty" , 5 : "fifty" , 6 : "sixty" , 7 : "seventy" , 8 : "eighty" , 9 : "ninety" , 0 : ""}   

    hundreds = {1 : "onehundred", 2 : "twohundred" , 3 : "threehundred" , 4 : "fourhundred" , 5 : "fivehundred" , 6 : "sixhundred" , 7 : "sevenhundred" , 8 : "eighthundred", 9 : "ninehundred",0 : ""}

    for i in range(1,n + 1):

        if i == 1000:

            total_length += len("onethousand")

        else:

            total_length += len(hundreds.get(i // 100))
            
            if  10 <= i % 100 < 20:

                total_length += len(teens.get(i % 100))

            else:

                total_length += len(tens.get((i % 100) // 10))

                total_length += len(ones.get(i % 10))

            if i > 100 and i % 100 != 0:

                total_length += len("and")

    return total_length


#Count number of letters
n = int(input("Enter a number less or equal to 1000: "))

print("Number of  letters: ",count_length_letters(n))     