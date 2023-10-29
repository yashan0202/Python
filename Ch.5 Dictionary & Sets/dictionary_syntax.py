# Use Curly Bracket to make Dictionary

myDict = {
    "Fast": "In a quick manner",
    "Slow": "In a low pace",
    "Yash": "Is a smart boy",
    "Marks": [34,45,12,69,10],
    "anotherDict":{'yash':'Good boy'}
    }

print(myDict["Slow"])
print(myDict["Marks"])
print(myDict["anotherDict"]["yash"])

myDict["Marks"]=[23,34,46,9,58] #we can change values.
print(myDict["Marks"])