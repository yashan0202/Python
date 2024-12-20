'''WAP to read a text from a given file and find out whether it contains the word "Twinkle" or not.'''

f = open("C:\\Users\\yashu\\Desktop\\Lavanya\\Python (CodeWithHarry)\\Python\\00_Chapters\\Ch.9 File I\O\\01_file.txt", "r")
content = f.read()
if "Twinkle" in content: #if twinkle , it will print not present because its lower case.
    print("Twinkle is present")
else:
    print("Twinkle is not present")

f.close()