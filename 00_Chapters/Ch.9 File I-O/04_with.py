f = open("C:\\Users\\yashu\\Desktop\\Lavanya\\Python (CodeWithHarry)\\Python\\00_Chapters\\Ch.9 File I-O\\01_file.txt", "r")
print(f.read())
f.close()

# The above code can be written in a more concise way using with open as follows:

with open("C:\\Users\\yashu\\Desktop\\Lavanya\\Python (CodeWithHarry)\\Python\\00_Chapters\\Ch.9 File I-O\\01_file.txt", "r") as f:
    a = f.read()
    print(a)

# The difference between the two methods is that in the first method, we have to close the file manually using f.close()
#  whereas in the second method, the file is automatically closed after the block of code is executed.

