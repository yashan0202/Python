class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is very good in {self.language} language")

class Programmer(Employee): # a new class Programmer is created which inherits the properties of Employee class
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is very good in {self.language} language")

a= Employee()
b= Programmer()

print(a.company)
print(b.company)