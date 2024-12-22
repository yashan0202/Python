'''
Override the __len__() method on vector of problem 5 to display the dimension of the vector. 
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
    
    def __len__(self):
        return 3

v1 = Vector(1, 2, 3)
print(len(v1)) # Output: 3

'''
But what if we want to find the length of the vector in n dimensions. We can modify the __len__() method to return the length of the vector in n dimensions.
we will take it in a list .

The above code can be also simplified as follows:
'''

class Vector:
    def __init__(self, l): 
        self.l = l

    def __len__(self):
        return len(self.l)
    
v1 = Vector([1,2,3]) # taking it in a list
print(len(v1)) # Output: 3

