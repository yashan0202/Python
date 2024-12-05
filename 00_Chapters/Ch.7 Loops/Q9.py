'''WAP to print multiplication table of n using
for loop in reversed order'''

n = int(input("Enter a number:"))

# Print the multiplication table of n in reversed order
for i in range(10, 0, -1):
    product = n * i
    print(f"{n} x {i} = {product}")


    