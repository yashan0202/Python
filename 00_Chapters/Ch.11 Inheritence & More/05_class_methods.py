# Class method "Self" ki jaga "cls" likha jata hai.

class Employee:
    company = "Google"

    @classmethod
    def show(cls):
        print(f"The company is {cls.company}")

e = Employee()
e.company = "Microsoft"

e.show() # Without using class method, it will print "Microsoft" as the output