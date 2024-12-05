'''WAP which finds out whether a given name is present in a 
list or not'''

list = ['yash','vidya','archana','amrendra']
name = input("Enter the word: ")

if name in list:
    print(name, "is present in the list")
else:
    print("Name is not present")