class Employee:
    name = "Yash"
    language = "Python"
    salary = 120000

    def getInfo(self):
        print(f"The name of the employee is {self.name} and his language is {self.language} and his salary is {self.salary}")

    @staticmethod # this allows to run the function without self or any parameter.
    def greet():
        print("Good Morning")

yash = Employee()
nandini = Employee()

yash.greet() # or Employee.greet(yash)
yash.getInfo() # or Employee.getInfo(yash)