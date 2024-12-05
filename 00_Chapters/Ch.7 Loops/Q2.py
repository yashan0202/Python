''' WAP to print multiplication table of a given 
number using for loop '''

a = int(input("Enter the number: "))
for i in range(1,11):
    result = a*i
    print(result)