'''
WAP in functions to covert celcius to fehrenheit
'''

# f = int(input("Enter temperature in Fehrenheit: "))
# c = 5*(f-32)/9

# print(f"The temperature in Celcius is {c}")

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in Fehrenheit: "))
c= f_to_c(f)

print(f"The temperature in Celcius is {round(c,2)}°C")