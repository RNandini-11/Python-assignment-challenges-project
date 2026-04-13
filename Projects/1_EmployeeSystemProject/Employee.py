class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

    def __repr__(self):
        return F'Employee(name={self.name}, age={self.age}, salary={self.salary}'

'''
e = Employee("Raj", 25, 50000)  #e = Employee(name="Raj", age=25, salary=50000) think like this
print(e)      #inside a obj - emp.name = "Raj", emp.age = 25, emp.salary = 50000
print(str(e)) #for str
print(repr(e)) #for repr
'''
