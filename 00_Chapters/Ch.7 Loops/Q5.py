'''WAP to find the sum of first n natural numbers
using while loop'''

num = int(input("Enter the number: "))
sum = 0
for i in range(1,num+1):
    sum = sum + i
print(sum)
    