class Employee:
    company = "Google"

    @classmethod
    def show(cls):
        print(f"The company is {cls.company}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, name):
        self.fname, self.lname = name.split(" ")

    
e = Employee()
e.company = "Microsoft"

e.name = "Yash Anand"
print(e.fname, e.lname)

e.show() 