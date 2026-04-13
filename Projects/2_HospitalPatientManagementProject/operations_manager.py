from specialization import *

class OperationsManager:
  def __init__(self):
    self.s=Specialization()
    self.menu()

  def menu(self):
    while True:
      print('\n______ Patient Menu ______')
      print('1. Add patient')
      print('2. List patients')
      print('3. Get next patient')
      print('4. Remove patient')
      print('5. Queue Capacity')
      print('6. Exit')

      try:
        choice = int(input('Enter your choice: '))
      except ValueError:
        print('Invalid input. Please enter a number.')
        continue


      if choice == 1:
        self.add_patient()
      elif choice == 2:
        self.list_patients()
      elif choice == 3:
        self.get_next_patient()
      elif choice == 4:
        self.remove_patient()
      elif choice == 5:
        self.check_queue_capacity()
      elif choice == 6:
        self.exiting()
        break
      else:
        print('Invalid choice. Please try again.')

  def add_patient(self):
    try:
      while True:
        no=int(input('How many patients to add:'))
        if no <= 0:
          print('Enter positive number...!')
          continue
        if not no:
          print('Cannot be empty...!')
          continue
        break
    except ValueError:
      print('Invalid input!')

    for i in range(no):
      print(f'\n----Enter details of patient {i+1}----')
      while True:
        name = input('Enter patient name: ')
        if name.isdigit():
          print('Name cannot contain digits...!')
          continue
        if not name:
          print('Name cannot be empty...!')
          continue
        break

      try:
        while True:
          status = int(input('Enter patient status (0 for normal) 0-2: '))
          if status < 0 or status > 2:
            print('Give proper status...!')
            continue
          break
      except ValueError:
        print('Invalid input!')
        continue

      self.s.add_patient(name,status)
      print('Patient added successfully...!')

  def list_patients(self):
    self.s.list_patients()

  def get_next_patient(self):
    self.s.get_next_patient()

  def remove_patient(self):
    while True:
      name = input('Enter patient name: ')
      if name.isdigit():
        print('Cannot contain digits...!')
        continue
      if not name:
        print('Name cannot be empty...!')
        continue
      break
    self.s.remove_patient(name)

  def check_queue_capacity(self):
    self.s.check_queue_capacity()

  def exiting(self):
      print('Thank you for using the Operations Manager...!')
      exit()


#om=OperationsManager()