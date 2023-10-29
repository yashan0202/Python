#we can create list using []
a = [1,2,4,56,69,100]

print(a)
print(a[0])
print(a[1:3])
print(a[0::2])
print(len(a))

# Change the value of element in the list
a[0] = 17
print(a)

# We can create a list of different types
b = ["apple", 69, 9.11, True]
print(b)
print(type(b))

# List Slicing
friends = ["Parth","Aditya","Harshil","Prakhar","BG","Nandini",45]
print(friends[0:4])
print(friends[-4:])