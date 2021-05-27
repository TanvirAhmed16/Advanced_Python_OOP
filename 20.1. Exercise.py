'''
# Adding some more dunder method by reading Python documentation.
'''

class Employee():
    def __init__(self, fname, lname, age, salary):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.salary = salary

    def show_employee_details(self):
        print(f'Employee Name: {self.fname} {self.lname}.')
        print(f'Employee age: {self.age} Years Old.')
        print(f'Employee Salary: {self.salary} BDT.')

    def __str__(self):
        return 'Show me employee details.'

    def __repr__(self):
        self.show_employee_details()
        return f'Showing Details.'

    def __add__(self, other):
        return self.salary + other.salary

    def __eq__(self, other):
        return self.age == other.age



emp1 = Employee('Tanvir', 'Ahmed', 25, 25000)
emp2 = Employee('Anower', 'Hossain', 25, 20000)

emp1.show_employee_details()
print(emp1.__str__())
print(emp1.__repr__())
print(emp1.__add__(emp2))
print(emp1.__eq__(emp2))