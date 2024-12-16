'''WAP which finds out whether a given name is present in a 
list or not'''

list = ['yash','vidya','archana','amrendra']
name = input("Enter the word: ")

if name in list:
    print(name, "is present in the list")
else:
    print("Name is not present")


# WAP to find whether a certain paragraph is talking about yash or not

para = input("Enter the paragraph: ")

if 'yash' in para.lower():
    print("Yash is present in the paragraph")
else:
    print("Yash is not present in the paragraph")