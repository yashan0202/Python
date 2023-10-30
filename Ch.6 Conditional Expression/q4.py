'''WAP to detect spam text from the following keyword:
"make a lot of money","buy now","subscribe now","click this".'''

# SPAM DETECTOR

text = input("Enter your message: ")
if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe now" in text):
    spam = True
elif("click this" in text):
    spam = True
else:
    spam = False

if spam:
    print ("This is a Spam Text")
else:
    print ("This is not a Spam Text")
