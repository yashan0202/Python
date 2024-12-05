'''WAP to take 3 numbers from users and find smallest and largest number'''

def smallest_largest(a,b,c):
    if a<b and a<c:
        print(f"The smallest number is {a}")
    elif b<a and b<c:
        print(f"The smallest number is {b}")
    elif c<a and c<b:
        print(f"The smallest number is {c}")
    
    if a>b and a>c:
        print(f"The largest number is {a}")
    elif b>a and b>c:
        print(f"The largest number is {b}")
    elif c>a and c>b:
        print(f"The largest number is {c}")

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
smallest_largest(a,b,c)


