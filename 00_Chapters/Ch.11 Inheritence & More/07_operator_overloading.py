'''
Operators in Python can be overloaded using dunder methods.
These methods are called when a given operator is used on the objects.
Operators in python can be overloaded using the following methods:

p1+p2 => p1.__add__(p2)
p1-p2 => p1.__sub__(p2)
p1*p2 => p1.__mul__(p2)
p1/p2 => p1.__truediv__(p2)
p1//p2 => p1.__floordiv__(p2)
p1**p2 => p1.__pow__(p2)
p1%p2 => p1.__mod__(p2)

str__() #used to convert the object into a string
'''

class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self,num):
        print(f"Lets add {self.n} and {num.n}")
        return self.n + num.n
    
a= Number(4)
b= Number(6)

print(a+b)