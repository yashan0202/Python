'''WAP to calculate the factorial of a given number
using for loop.'''

# n! = 1 X 2 X 3 X 4 X........... X n
# 5! = 1 X 2 X 3 X 4 X 5

num = int(input("Enter the number: "))
factorial = 1 #because we initialize adition with 0 and multiplication with 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}") # or print(factorial)
