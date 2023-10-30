'''WAP to find whether a given username contains less 
than 10 characters or not.'''

username = input("Enter your username: ")
if len(username) <= 10:
    print("Username is Valid")
else:
    print("Invalid username because less than 10 characters.")