class Employee:
    def __init__(self):
        print("Constructor of Employee class")    
    a=1

class Programmer(Employee):
    def __init__(self):
        super().__init__() # super() is used to call the constructor of the parent class
        print("Constructor of Programmer class")
    b=2

class Manager(Programmer):
    def __init__(self):
        super().__init__() # super() is used to call the constructor of the parent class
        print("Constructor of Manager class")
    c=3

# obj1 = Employee() 
# print(obj1.a)

# obj2 = Programmer()
# print(obj2.a, obj2.b) 

obj3 = Manager()
print(obj3.a, obj3.b, obj3.c)

 

