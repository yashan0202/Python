'''
Remove every empty space from the string and print it.
'''

txt = input("Enter a string: ")
a =[]
a = txt.split()
print(a)
print("Ans is:",''.join(a))

'''
Remove every empty space from the string without any function and print it.
'''

txt = input("Enter a string: ")  # Take input from the user
new_txt = ""  # Initialize an empty string to store the result

for char in txt:  # Iterate through each character in the input string
    if char != " ":  # If the character is not a space
        new_txt += char  # Add the character to the new string

print("String without spaces:", new_txt)  # Print the final result

'''
Now only keep 1 space and remove the rest of the empty spaces in a string.
'''

txt = input("Enter a string: ")  
new_txt = ""  
space_flag = False  # Flag to track spaces

for char in txt:  
    if char != " ": 
        new_txt += char  
        space_flag = True  # Set flag to indicate a word is being processed
    else:
        if space_flag:  # Only add a single space if the last character was not a space
            new_txt += " "
            space_flag = False  # Reset the flag to prevent extra spaces

print("Final String is:", new_txt)  

