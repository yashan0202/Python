'''WAP to mine a log file and find out whether it contains the 'python' keyword or not and at which line number.'''

with open("C:\\Users\\yashu\\Desktop\\Lavanya\\Python (CodeWithHarry)\\Python\\00_Chapters\\Ch.9 File I-O\\Q6_txt.log") as f:
    content = f.readlines()

lines = 1
for line in content:
    if 'python' in line.lower():
        print(f"Yes, Python is present in the log file at line number {lines}")
        break

    lines += 1

else:
    print("No, Python is not present in the log file")