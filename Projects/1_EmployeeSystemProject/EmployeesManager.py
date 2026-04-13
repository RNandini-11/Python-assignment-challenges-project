from Employee import *
from tabulate import tabulate

class EmployeesManager:
    def __init__(self):
        self.employees=[]
        '''It is not a list of tuples, it is a list of objects.
        Each object has attributes, so we access and update them using dot notation like emp.salary.'''

    def add_employee(self, name, age, salary):
        emp = Employee(name, age, salary)
        self.employees.append(emp)    #self.employees = [emp1, emp2]  <- self.employees contains [ Employee_object, Employee_object ]

    def list_employees(self):
        if not self.employees:
            print("No employees found.")
            return #return immediately exits the method.
        table = []
        for emp in self.employees: # emp = actual Employee object
            table.append([emp.name, emp.age, emp.salary])
        print("\n======= EMPLOYEE LIST =======\n")
        print(tabulate(table, headers=["Name", "Age", "Salary"], tablefmt="grid"))
        print('Employees listed successfully...!')

    def delete_by_age_range(self, min_age, max_age):
        before = len(self.employees)
        self.employees = [
            emp for emp in self.employees
            if not (min_age <= emp.age <= max_age)
        ]
        after = len(self.employees)
        if after < before:
            print(f"{before - after} employee(s) deleted successfully...!")
        else:
            print("No employees found in the specified age range")

    def find_employee(self, name):
        found=False
        table = []
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                table.append([emp.name, emp.age, emp.salary])
                print("\n------- Find employee -------\n")
                print(tabulate(table, headers=["Name", "Age", "Salary"], tablefmt="grid"))
                found=True
                print('Employee found successfully...!')
        if not found:
            print("Employee not found.")

    def update_salary(self, name, new_salary):
        for emp in self.employees:           # emp = actual Employee object so emp.salary = 70000 directly updates that object
            if emp.name.lower() == name.lower():
                emp.salary = new_salary
                print("Salary updated successfully...!")
                return #return immediately exits the method.
        print("Employee not found")

'''
em=EmployeesManager()
em.add_employee("Raj", 25, 50000)
em.add_employee("Amit", 30, 60000)
em.list_employees()
em.delete_by_age_range(20, 26)
em.list_employees()
em.find_employee("Amit")
em.update_salary("Amit", 70000)
em.list_employees()
'''