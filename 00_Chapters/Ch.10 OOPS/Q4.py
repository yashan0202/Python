'''
Add a static method in problem 2 to greet the user with "Good Morning".
'''

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

    @staticmethod
    def greet():
        print("Good Morning")

a = Calculator(4)

Calculator.greet()

a.square()
a.cube()
a.square_root()
