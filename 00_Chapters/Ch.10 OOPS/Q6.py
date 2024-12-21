'''
Can you change the self-parameter inside a class to something else
(say "slf"). Try changing it and see if it works.
'''

class Employee:
    def __init__(slf, name, age, salary):
        slf.name = name
        slf.age = age
        slf.salary = salary

    def printDetails(slf):
        print(f"The name of the employee is {slf.name}. He is {slf.age} years old and his salary is {slf.salary}")

y = Employee("Yash", 21, 120000)
print(y.printDetails()) 
