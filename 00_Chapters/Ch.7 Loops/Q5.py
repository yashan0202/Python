'''WAP to find the sum of first n natural numbers
using while loop'''

num = int(input("Enter the number: "))
sum = 0
for i in range(1,num+1):
    sum = sum + i
print(sum)


#while loop

num = int(input("Enter the number: "))
sum = 0
i = 1
while i <= num:
    sum = sum + i
    i = i + 1
print(sum)
