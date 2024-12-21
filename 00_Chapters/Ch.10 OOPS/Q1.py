'''
Create a class "Programmer" for storing information of few programmers working at Microsoft.
'''

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

a = Programmer("Yash", 120000, 1234)
print(a.company, a.name, a.salary, a.pin)
b = Programmer("Nandini", 130000, 1235)
print(b.company, b.name, b.salary, b.pin)


