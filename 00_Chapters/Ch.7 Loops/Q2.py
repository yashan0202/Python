''' WAP to print multiplication table of a given 
number using for loop '''

a = int(input("Enter the number: "))
for i in range(1,11):
    result = a*i
    print(result)

#or

a = int(input("Enter the number you want multiplication of: "))
for a in range(0,(a*10)+1,a):
    print(a)

#or
a = int(input("Enter the number you want multiplication of: "))
for i in range(1,11):
    print(f"{a} X {i} = {a*i}")