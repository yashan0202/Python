'''
WA python function to print first n lines of the following pattern:
***
**
*
for n=3
'''

def pattern(n):
    if n==0:
        return
    print("*"*n) #n jitni baar hai utni baar * print karega
    pattern(n-1) #fir n-1 * print karega zero tak, zero aane ke baad terminate ho jayega

n = int(input("Enter the number: "))
pattern(n)

# if you want to print the pattern in reverse order just use (n+1), no it wont work but try.