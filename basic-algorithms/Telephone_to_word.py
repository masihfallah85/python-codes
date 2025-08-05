#Telephone_to_word.py

"""
In this script we turna telephone numebr to all possible words associated to it based on this translation rules:
2 -> a , b , c
3 -> d ,  e , f
4-> g , h , i
5 -> j , k , l
6 -> m , n , o
7 -> p,,r,s
8 -> t  , u , v
9 -> w  , x , y
"""

def translate(phone_number):

    """This fucntion translates phone number to word based on above rules"""

    result = []

    if len(phone_number) == 1 and phone_number == "2":

        result = ["a","b","c"]

        return result
    
    elif len(phone_number) == 1 and phone_number == "3":

        result = ["d","e","f"]

        return result
    
    elif len(phone_number) == 1 and phone_number == "4":

        result = ["g","h","i"]

        return result
    
    elif len(phone_number) == 1 and phone_number == "5":

        result = ["j","k","l"]

        return result

    elif len(phone_number) == 1 and phone_number == "6":

        result = ["m","n","o"]

        return result
    
    elif len(phone_number) == 1 and phone_number == "7":

        result = ["p","r","s"]

        return result
    
    elif len(phone_number) == 1 and phone_number == "8":

        result = ["t","u","v"]

        return result
    
    elif len(phone_number) == 1 and phone_number == "9":

        result = ["w","x","y"]

        return result
    
    elif phone_number[0] == "2":

        rest_of_number = phone_number[1:]

        for i in  translate(rest_of_number):

            result.append("a" + i)

        for i in translate(rest_of_number):

            result.append("b" + i)

        for i in translate(rest_of_number):

            result.append("c" + i)

    elif phone_number[0] == "3":

        rest_of_number = phone_number[1:]

        for i in  translate(rest_of_number):

            result.append("d" + i)

        for i in translate(rest_of_number):

            result.append("e" + i)

        for i in translate(rest_of_number):

            result.append("f" + i)

    elif phone_number[0] == "4":

        rest_of_number = phone_number[1:]

        for i in  translate(rest_of_number):

            result.append("g" + i)

        for i in translate(rest_of_number):

            result.append("h" + i)

        for i in translate(rest_of_number):

            result.append("i" + i)

    elif phone_number[0] == "5":

        rest_of_number = phone_number[1:]

        for i in  translate(rest_of_number):

            result.append("j" + i)

        for i in translate(rest_of_number):

            result.append("k" + i)

        for i in translate(rest_of_number):

            result.append("l" + i)

    elif phone_number[0] == "6":

        rest_of_number = phone_number[1:]

        for i in  translate(rest_of_number):

            result.append("m" + i)

        for i in translate(rest_of_number):

            result.append("n" + i)

        for i in translate(rest_of_number):

            result.append("o" + i)

    elif phone_number[0] == "7":

        rest_of_number = phone_number[1:]

        for i in  translate(rest_of_number):

            result.append("p" + i)

        for i in translate(rest_of_number):

            result.append("r" + i)

        for i in translate(rest_of_number):

            result.append("s" + i)

    elif phone_number[0] == "8":

        rest_of_number = phone_number[1:]

        for i in  translate(rest_of_number):

            result.append("t" + i)

        for i in translate(rest_of_number):

            result.append("u" + i)

        for i in translate(rest_of_number):

            result.append("v" + i)

    elif phone_number[0] == "9":

        rest_of_number = phone_number[1:]

        for i in  translate(rest_of_number):

            result.append("w" + i)

        for i in translate(rest_of_number):

            result.append("x" + i)

        for i in translate(rest_of_number):

            result.append("y" + i)

    return result

#Prompt user to input the phone number
phone_number = input("Enter a phone number: ")

#Print the result
print(f"Possible words associated to number {phone_number}")

for word in translate(phone_number):

    print(word)