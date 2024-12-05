'''WAP to print the below Star pattern:
*
**
***
****
'''

star = int(input("How many Stars you want to print: "))
for i in range(0,star+1):
    print("*" * i)