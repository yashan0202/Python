'''
factorial(n) = n X n-1 X ...... 3 X 2 X 1 

factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if (n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number : "))
print(f"The factorial of {n} is {factorial(n)}")       