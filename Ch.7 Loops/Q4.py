'''WAP to find whether a number is prime or not'''

num = int(input("Enter the number: "))
prime = True

for i in range(2,num):
    if (num % i == 0):
        prime = False
        break

if prime:
    print(num," is a Prime Number")
else:
    print(num," is NOT a Prime Number")

