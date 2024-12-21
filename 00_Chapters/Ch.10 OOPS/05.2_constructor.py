class Employee:
    name = "Yash"
    language = "Python"
    salary = 120000

    def __init__(self,name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary 
        print("The constructor is created")

yash = Employee("Yashu","Python",120000)
print(yash.name,yash.salary,yash.language)

nandini = Employee("Nandini","Java",130000)