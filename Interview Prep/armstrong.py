a = int(input('Enter the number: '))
n = len(str(a))
temp = a
sum =0
while a>0:
    digit = a%10
    sum = sum + digit**n
    a = a//10

if temp == sum:
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')
    
