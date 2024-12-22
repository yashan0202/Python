'''
Create a class "Employee" and add salary and increment properties to it.
Add a method 'salaryAfterIncrement' method with a @property decorator with
a setter which changes the value of increment based on the salary.
'''

class Employee:
    salary = 500
    increment = 10 #that is 10 percent

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment / 100)) #formula for increment
    

e = Employee()
print(e.salaryAfterIncrement)