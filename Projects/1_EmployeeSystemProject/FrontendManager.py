from EmployeesManager import *

class FrontendManager:
    def __init__(self):
        self.em=EmployeesManager()
        self.menu()

    def menu(self):
        while True:
            print('\n______ Employee Menu ______')
            print('1. Add Employee')
            print('2. List Employees')
            print('3. Delete by Age Range')
            print('4. Find Employee')
            print('5. Update Salary')
            print('6. Exit')

            try:
                choice = int(input('Enter your choice: '))
            except ValueError:
                print('Invalid choice!')
                continue

            if choice == 1:
                self.add_employee()
            elif choice == 2:
                self.list_employees()
            elif choice == 3:
                self.delete_by_age_range()
            elif choice == 4:
                self.find_employee()
            elif choice == 5:
                self.update_salary()
            elif choice == 6:
                self.exiting()
                break
            else:
                print('Invalid choice!')


    def add_employee(self):
        try:
            no=int(input('How many employees to add:'))
        except ValueError:
            print('Invalid input!')

        for i in range(no):
            print(f'\n----Enter details of employee {i+1}----')
            while True:
                name = input('Name:')
                if not name:
                    print("Name cannot be empty...!")
                    continue
                if any(char.isdigit() for char in name):
                    print("Name cannot contain numbers...!")
                    continue
                break

        try:
            while True:
                age = int(input('Age:'))
                salary = float(input('Salary:'))
                if age < 0 :
                    print('Age cannot be negative...!')
                    continue
                if salary < 0 :
                    print('Salary cannot be negative...!')
                    continue
                break
        except ValueError:
            print('Invalid input!')
        self.em.add_employee(name, age, salary)
        print('Employee added successfully...!')

    def list_employees(self):
        self.em.list_employees()

    def delete_by_age_range(self):
        try:
            while True:
                min_age = int(input('Enter minimum age:'))
                max_age = int(input('Enter maximum age:'))
                if min_age < 0 :
                    print('Age cannot be negative...!')
                    continue
                if max_age < 0 :
                    print('Age cannot be negative...!')
                    continue
                if min_age > max_age:
                    print('Minimum age cannot be greater than maximum age...!')
                    continue
                break
        except ValueError:
            print('Invalid input!')
        self.em.delete_by_age_range(min_age, max_age)

    def find_employee(self):
        while True:
            name = input('Enter employee name to find details:')
            if not name:
                print("Name cannot be empty...!")
                continue
            if name.isdigit():
                print("Name cannot contain numbers...!")
                continue
            break
        self.em.find_employee(name)

    def update_salary(self):
        while True:
            name = input("Enter employee name: ")
            if not name:
                print("Name cannot be empty...!")
                continue
            if name.isdigit():
                print("Name cannot contain numbers...!")
                continue
            break

        try:
            new_salary = float(input("Enter new salary: "))
        except ValueError:
            print('Invalid salary!')
        self.em.update_salary(name, new_salary)

    def exiting(self):
        print('Thank you for using the system.')
        exit()

