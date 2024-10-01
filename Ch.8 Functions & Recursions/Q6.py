'''
WAP in functions to convert inches to cm
'''

def inches_to_cm(i):
    return i*2.54

i = int(input("Enter length in inches: "))
c= inches_to_cm(i)

print(f"The length in cm is {round(c,2)} cms")