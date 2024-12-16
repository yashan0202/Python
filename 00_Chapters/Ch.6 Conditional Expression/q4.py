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


#or

p1= "make a lot of money"
p2= "buy now"
p3= "subscribe now"
p4= "click this"

text = input("Enter your message: ")
if(p1 in text or p2 in text or p3 in text or p4 in text):
    print("This is a Spam Text")
else:
    print("This is not a Spam Text")
