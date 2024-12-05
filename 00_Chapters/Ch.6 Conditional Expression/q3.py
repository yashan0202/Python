'''WAP to find out whether a student is pass or fail, 
if it requires total of 40% and atleast of 33% in each 
subject to pass. Assume 3 subjects and take marks as 
an input from the user'''

sub1 = int(input("Enter first subject marks: "))
sub2 = int(input("Enter second subject marks: "))
sub3 = int(input("Enter third subject marks: "))

if (sub1<=33 or sub2<=33 or sub3<=33):
    print("Fail")

elif ((sub1 + sub2 + sub3) / 3 <= 40):
    print("Fail")

else:
    print("Pass")