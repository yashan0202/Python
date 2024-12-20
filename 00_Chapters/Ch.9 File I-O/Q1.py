'''3 WAP to read lines via while loop'''

f = open("C:\\Users\\yashu\\Desktop\\Lavanya\\Python (CodeWithHarry)\\Python\\00_Chapters\\Ch.9 File I-O\\01_file.txt", "r")


line=f.readline()
while (line!=""):
    print(line)
    line=f.readline()

f.close()