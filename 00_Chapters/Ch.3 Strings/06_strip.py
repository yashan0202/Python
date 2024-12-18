#Strip function removes the leading and trailing whitespaces from a string

#1 Left strip/ Leading strip
s = "   yash  "
print(s.lstrip())


#2 Right strip/ Trailing strip
s = "   yash  "
print(s.rstrip())


#3 Strip
str = '    Hello! Welcome Home.   '
print(str)
print(str.strip())


#4 Strip with argument
string = '   ....aaaToppr learningaa....   '
print(string.strip('.a')) # Leading and trailing whitespaces are not removed
print(string.strip(' .a')) # All , ., a characters in the left and right of string are removed


#5
string = 'malayalam'
print(string.strip('ma')) # Leading and trailing whitespaces are removed