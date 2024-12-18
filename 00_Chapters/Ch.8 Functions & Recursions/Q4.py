'''
WA recursive function to print the sum of first n natural number

sum(1) = 1
sum(2) = 1 + 2 = 3
sum(3) = 1 + 2 + 3 = 6
sum(4) = 1 + 2 + 3 + 4 = 10
sum(5) = 1 + 2 + 3 + 4 + 5 = 15
sum(n) = 1 + 2 + 3 + 4 + 5 + ....... + n
sum(n) = n + sum(n-1) 
'''

def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
    
n = int(input("Enter the number: "))
print("The sum of first",n,"natural number is: ",sum(n))

    
