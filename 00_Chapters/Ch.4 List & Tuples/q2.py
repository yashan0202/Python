#WAP to accept marks of 6 students and display them in a sorted manner.

m1 = int(input("Enter marks of Student 1: "))
m2 = int(input("Enter marks of Student 2: "))
m3 = int(input("Enter marks of Student 3: "))
m4 = int(input("Enter marks of Student 4: "))
m5 = int(input("Enter marks of Student 5: "))
m6 = int(input("Enter marks of Student 6: "))

l1=[m1,m2,m3,m4,m5,m6]
l1.sort()
print(l1)