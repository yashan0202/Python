'''
Write a class "calculator" capable of finding square, cube and square root of a number.
'''

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of {self.n} is {self.n ** 2}")  

    def cube(self):
        print(f"The cube of {self.n} is {self.n ** 3}")

    def square_root(self):
        print(f"The square root of {self.n} is {self.n ** 0.5}")

a = Calculator(4)
a.square()
a.cube()
a.square_root()

'''
Agar normally karna hota toh aise karte: 

n = int(input("Enter the number: "))
square = n**2
cube = n**3
root = n**0.5

print(f"The square of {n} is {square}, The cube is {cube} and Root is {root}")

'''