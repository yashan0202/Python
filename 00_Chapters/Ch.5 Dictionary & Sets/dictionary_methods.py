myDict = {
    "Fast": "In a quick manner",
    "Slow": "In a low pace",
    "Yash": "Is a smart boy",
    "Marks": [34,45,12,69,10],
    "anotherDict":{'yash':'Good boy'},
    9:11
    }

# LHS = Keys & RHS = Values. Each key has its corresponding values.

#print(myDict)
print(myDict.keys())         #1
print(type(myDict.keys())) 

print(myDict.values())       #2

print(myDict.items())        #3

updateDict = {
    'Divya':'Sister',
    'Archana':'Mother',
    'Ved':'Brother'
}
myDict.update(updateDict)    # Updates the Dictionary
print(myDict)                #4

print(myDict.get('yash'))    #5
print(myDict.get('Yash'))