class Employee:
    name = "Default name"
    salary = 100
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the language, your language is {self.language}")

class Programmer(Employee,Coder): # a new class Programmer is created which inherits the properties of Employee & Coder class
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is very good in {self.language} language")

a= Employee()
b= Programmer()

b.show()
b.printLanguage()
b.showLanguage()