''' WAP to find greatest of four numbers entered by the user '''

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num4):
    f1=num1
else:
    f1=num4

if(num2>num3):
    f2=num2
else:
    f2=num3

if(f1>f2):
    print("The Greatest Number is ",f1)
else:
    print("The Greatest Number is ",f2)


#or

n1= int(input("Enter number: "))
n2= int(input("Enter number: "))
n3= int(input("Enter number: "))
n4= int(input("Enter number: "))

if n1>n2 and n1>n3 and n1>n4:
    print(n1, "is the greatest")
    
elif n2>n1 and n2>n3 and n3>n4:
    print(n2, "is the greatest")
    
elif n3>n1 and n3>n2 and n3>n4:
    print(n3, "is the greatest")
    
else:
    print(n4, "is the greatest")

