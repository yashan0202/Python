'''WAP to find out whether a file is identicle and matches the content of another file or not.'''

with open("C:\\Users\\yashu\\Desktop\\Lavanya\\Python (CodeWithHarry)\\Python\\00_Chapters\\Ch.9 File I-O\\Q7_txt1.txt") as f:
    content1 = f.read()

with open("C:\\Users\\yashu\\Desktop\\Lavanya\\Python (CodeWithHarry)\\Python\\00_Chapters\\Ch.9 File I-O\\Q7_txt2.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("Both files are identical")
else:
    print("Both files are not identical")
    