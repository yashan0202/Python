a = None                #1
if (a is None):
    print("yes")
else:
    print("no")


b = [45,55,9,18]         #2
print(45 in b)


# example of in operator
# list of fruits
fruits = ["apple","banana","mango","orange"]
if "apple" in fruits:
    print("Apple is present")
else:
    print("Apple is not present")

# example of not in operator
# list of fruits
fruits = ["apple","banana","mango","orange"]
if "apple" not in fruits:
    print("Apple is not present")
else:
    print("Apple is present")

# example of is operator
# check if a variable is an integer or not
age = 25
if isinstance(age,int):
    print("It is an integer")
else:
    print("It is not an integer")

# example of is not operator
# check if a variable is an integer or not
age = 25.0
if not(isinstance(age,int)):
    print("It is not an integer")
else:
    print("It is an integer")