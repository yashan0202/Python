f = open("C:\\Users\\yashu\\Desktop\\Lavanya\\Python (CodeWithHarry)\\Python\\00_Chapters\\Ch.9 File I-O\\01_file.txt", "r")

'''1 readline() function'''

lines = f.readlines()
print(lines,type(lines))


'''2 read line by line'''

line1 = f.readline()
print(line1, type(line1))
line2 = f.readline()
print(line2, type(line2))
line3 = f.readline()
print(line3, type(line3))
line4 = f.readline()
print(line4, type(line4))
line5 = f.readline()
print(line5=="") # This will return True as there is no line left to read, line 5 is an empty string

f.close()



