class Employee:
    name = "Yash"
    language = "Python"  #this is a class attribute
    salary = 120000

yash = Employee()
print(yash.language,yash.salary)

nandini = Employee()
nandini.language = "Java"  #this is an instance attribute
print(nandini.language,nandini.salary,nandini.name) 