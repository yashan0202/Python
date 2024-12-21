'''
__init__() is a special method in which is first run as soon as the object is created.
__init__() is also known as a constructor.
It takes self-argument and can also take further arguments. 
'''

class Employee:
    name = "Yash"
    language = "Python"
    salary = 120000

    def __init__(self): # dunder method which is called automatically.
        print("The constructor is created")

    # def getInfo(self):
    #     print(f"The name of the employee is {self.name} and his language is {self.language} and his salary is {self.salary}")

    # @staticmethod 
    # def greet():
    #     print("Good Morning")

yash = Employee()
yash.name = "Yashu"
print(yash.name,yash.salary)

nandini = Employee() # this will also print the constructor message. Every time an object is created, the constructor is called.