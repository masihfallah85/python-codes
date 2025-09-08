#Complex_class.py

"""
In this script we define a custom complex class
"""

class Complex:

    def __init__(self,real,imaginary):

        self.real = real

        self.imaginary = imaginary

    def __str__(self):

        return f"{self.real}+{self.imaginary}i"
    
    def __repr__(self):

        return f"{self.real}+{self.imagianry}i"
    
    def _to_complex(self,number):

        if isinstance(number,Complex):

            return number
        
        elif isinstance(number,(int,float)):

            return Complex(number,0)
        
        else:

            raise TypeError(f"unsupported type : {type(number)}")
    
    def __add__(self,number_2):
        

        number_2._to_complex(number_2)

        self.real += number_2.real

        self.imaginary += number_2.imaginary

        return self

    def __mul__(self,number_2):

        number_2._to_complex(number_2)

        self.real = self.real * number_2.real - self.imaginary * number_2.imaginary

        self.imagianry = self.real * number_2.imaginary + self.imaginary * number_2.real

        return self
    
    def __sub__(self,number_2):

        number_2._to_complex(number_2)

        self.real -= number_2.real

        self.imaginary -= number_2.imaginary

        return self
    
    def __truediv__(self,number_2):

        number_2._to_complex(number_2)

        denom = number_2.real ** 2 + number_2.imaginary ** 2

        if denom == 0:

            raise ZeroDivisionError("Division by zero is invalid")
        
        self.real =  (self.real * number_2.real + self.imaginary * number_2.imaginary) / denom

        self.imagianry = (self.imaginary * number_2.real - self.real * number_2.imaginary) / denom

        return self
    
    def conjugate(self):

        self.imaginary *= -1

        return self
    
    def magnitude(self):

        return (self.real ** 2 + self.imaginary ** 2) ** 1/2
    

number = Complex(3,2)

number_2 = Complex(2,3)

print(number)

print(number_2 + number)

print(number_2 - number)

print(number_2 * number)

print(number_2 / number)

print(number_2.conjugate())

print(number.magnitude())
