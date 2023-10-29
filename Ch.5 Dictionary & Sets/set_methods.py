# Creating an empty set

a = set()
print(a)
print(type(a))

# Ading values to an empty set

a.add(3)
a.add('yash')
a.add(10)
a.add((2,3,4))
print(a)

print(len(a))

a.remove(10)
print(a)

print(a.pop())

print(a.clear())