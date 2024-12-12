story = "once upon a time there lived a boy named Thermo Dynamics"

print(len(story)) # length of the string

print(story.endswith("boy")) # returns True if the string ends with the given string

print(story.count("e")) # counts the number of times the given string is present in the main string

print(story.capitalize()) # capitalizes the first letter of the string

print(story.find("Thermo")) # returns the index of the given string

print(story.replace("boy", "smart boy")) # replaces the given string with the new string

print(story.title()) # capitalizes the first letter of each word in the string

##

st="This is a string with double  spaces"
doubleSpace = st.find("  ")
print(doubleSpace)