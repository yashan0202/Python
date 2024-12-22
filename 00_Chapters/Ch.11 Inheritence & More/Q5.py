'''
Write a class vector representing a vector of n dimensions. Overload the operators + and * to add and find the . product of two vectors.
'''

class Vector:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self,other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"Vector({self.x},{self.y},{self.z})"
    
# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print(v1 + v2) # Output: Vector(5,7,9)
print(v1 * v2) # Output: 32

print(v1 + v3) # Output: Vector(8,10,12)
print(v1 * v3) # Output: 50

'''
1. Take class Vector and initialize it with x, y, z.
2. Define __add__ method to add two vectors.
3. Define __mul__ method to multiply two vectors.
4. Define __str__ method to return the string representation of the vector.
5. Create two vectors v1 and v2.
6. Add v1 and v2 and print the result.
7. Multiply v1 and v2 and print the result.

'''


        