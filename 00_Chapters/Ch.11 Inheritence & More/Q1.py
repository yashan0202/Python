'''
Create a class (2D vector) and use it to create another class representing a 3D vector.
'''

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"The vector is {self.x}x + {self.y}y")    

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y) # This will call the constructor of the parent class.
        self.z = z

    def show(self):
        print(f"The vector is {self.x}x + {self.y}y + {self.z}z")

v2 = Vector2D(1, 2)
v2.show()
v3 = Vector3D(1, 2, 3)
v3.show()