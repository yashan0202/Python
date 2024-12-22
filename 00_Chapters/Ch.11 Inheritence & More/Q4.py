'''
Write a class 'Complex' to represent complex numbers along with overloaded operator
'+' and '*' which adds and multiply them.
'''

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, num):
        return Complex(self.real + num.real, self.imag + num.imag)
    
    def __mul__(self, num):
        return Complex(self.real * num.real - self.imag * num.imag, self.imag * num.real)
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
print(c1 * c2)
                       
