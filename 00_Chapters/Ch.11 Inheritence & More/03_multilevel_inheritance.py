# Example Syntax:

class Employee:                     # Parent class
    a=1

class Programmer(Employee):         # Child class
    b=2

class Manager(Programmer):          # Grandchild class
    c=3

obj1 = Employee()                   # Creating the objects
obj2 = Programmer()
obj3 = Manager()

print(obj1.a)                       # obj1.b and obj1.c has no attribute 'b' and 'c' , if we try to print them it will give an error
print(obj2.a, obj2.b)               # obj2.c has no attribute 'c'
print(obj3.a, obj3.b, obj3.c)