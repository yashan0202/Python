'''A file contains a word "Donkey" multiple times. You need to write a program which reads and replaces this word with "######" and 
   writes it back to the file.'''

f = open("C:\\Users\\yashu\\Desktop\\Lavanya\\Python (CodeWithHarry)\\Python\\00_Chapters\\Ch.9 File I-O\\01_file.txt", "r")
data = f.read()
replace = data.replace("Donkey", "######")
print(replace)
f.close()
