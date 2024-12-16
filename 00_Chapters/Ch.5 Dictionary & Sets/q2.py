'''Wap to input eight numbers from the user and 
display all the unique numbers '''

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))
num4 = int(input("Enter number 4:"))
num5 = int(input("Enter number 5:"))
num6 = int(input("Enter number 6:"))
num7 = int(input("Enter number 7:"))
num8 = int(input("Enter number 8:"))

set = {num1,num2,num3,num4,num5,num6,num7,num8}
print(set.union()) 

#or
print(set) #beacuse sets already remove the repetative elements.