'''WAP to find whether a given username contains less 
than 10 characters or not.'''

username = input("Enter your username: ")
if len(username) <= 10:
    print("Username is Valid")
else:
    print("Invalid username because less than 10 characters.")


#or

a = input("Enter your name: ")
b = len(a)

if b<10:
    print("the username has less than 10 char")
    
elif b == 10:
    print("perfectly balanced")
    
else:
    print("this has more than 10 char")