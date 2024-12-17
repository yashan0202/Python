a = int(input("Enter the number: "))

for i in range (2, a):
    if a % i == 0:
        print("Not a prime number")
        break

else:
    print("Prime number")