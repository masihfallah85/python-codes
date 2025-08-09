#Word_equvulant_of_check_amount.py

"""
In this script we use dictionary to translate check value less than 1000 to it's word representation.
"""

def translate(number):

    """This function gets a number as string and return it's word translation"""

    words = ""
    
    hundred = number // 100

    ten = (number % 100) // 10

    decimala_nomerator = number - int(number)

    one = number % 10 - decimala_nomerator

    decimal_denominator = 10 ** len(str(decimala_nomerator))

    hundreds = {
        
        0 : "",
        1 : "One hundred and ",
        2 : "Two hundreds and ",
        3 : "Three hundreds and ",
        4 : "Four hundreds and ",
        5 : "Five hundreds and ",
        6 : "Six hundreds and ",
        7 : "Seven hundreds and ",
        8 : "Eight hundreds and ",
        9 : "Nine hundreds and "
    }

    teens = {
        1 : "eleven and ",
        2 : "twelve and ",
        3 : "thirteen and ",
        4: "fourteen and ",
        5 : "fifteen and ",
        6 : "sixteen and ",
        7 : "seventeen and ",
        8 : "eighteen and ",
        9 : "nineteen and "
    }

    tens = {
        0 : "",
        2 : "twenty and ",
        3 : "thirty and  ",
        4 : "fourty and ",
        5 : "fifty  and ",
        6 : "sixty and ",
        7 : "seventy and ",
        8 : "eighty and ",
        9 : "ninety and "
    }

    ones = {
        0 : "",
        1 : "one and ",
        2 : "two and ",
        3 : "three and ",
        4 : "four and ",
        5 : "five and ",
        6 : "six and ",
        7 : "seven and ",
        8 : "eight and ",
        9 : "nine and "
    }

    words += hundreds[hundred]

    if ten == 1:

        words += teens[one]

    else :

        words += tens[ten]

        words += ones[one]

    if decimala_nomerator == 0:

        return words
    
    else:

        words += str(decimala_nomerator) + "/" + str(decimal_denominator)

        return words

#Prompt user to input check value
number = float(input("Enter check value below 1000: "))

#Print the result
print(f"{number} : {translate(number)}")