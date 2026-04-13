class Patient:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return f"Name: {self.name}, Status: {self.status}"

    def __repr__(self):
        return F'Patient(name={self.name}, status={self.status}'


'''
p = Patient("Raj", 2)  #p = Patient(name="Raj", status=2) think like this
print(p)                         #inside a obj - p.name = "Raj", emp.status = 2
'''