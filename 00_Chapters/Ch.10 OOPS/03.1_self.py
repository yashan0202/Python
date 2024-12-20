# Self refers to the instance of the class. It is automatically passed
# with a function call from an object.

class Employee:
    name = "Yash"
    language = "Python"
    salary = 120000

    def getInfo(self):
        print(f"The name of the employee is {self.name} and his language is {self.language} and his salary is {self.salary}")

    def greet(self):
        print("Good Morning")

yash = Employee()
nandini = Employee()

yash.greet() # or Employee.greet(yash)
yash.getInfo() # or Employee.getInfo(yash)