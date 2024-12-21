'''
Create a class with a class attribute a; create an object from it and set a directly using object.a = 0. Does this change the class attribute?
'''

class Demo: #'''Class Attributes'''
    a = 10

obj = Demo() #'''Instance Attributes'''
print(obj.a) # Prints the class attribute value because instance attribute is not defined.

obj.a = 0
print(obj.a) # Prints the instance attribute value.

print(Demo.a) # Prints the class attribute value because instance attribute is not defined.

# Hence, NO , the class attribute is not changed. The instance attribute is created and the class attribute remains the same.