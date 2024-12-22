'''
Create a class 'Pets' from a class 'Animals' and further create a class 'Dog'
from 'Pets'. Add a method 'bark' to class 'Dog'.
'''

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    def bark(self):
        print("Dog barks bow bow !")

d = Dog()
d.bark()