from patient import *
from tabulate import tabulate

class Specialization:
  def __init__(self):
    self.queue = []

  def add_patient(self, name, status):
    p=Patient(name,status)
    if p.status == 0:
      self.queue.insert(0, p)
    elif p.status == 1:
      for i, patient in enumerate(self.queue):
        if patient.status == 2:
            self.queue.insert(i, p)
            return
      self.queue.append(p)
    if p.status == 2:
        self.queue.append(p)


  def list_patients(self):
    if not self.queue:
        print("No patient found.")
        return #return immediately exits the method.
    table = []
    for p in self.queue: # p = actual patient object
        table.append([p.name, p.status])
    print("\n======= Patient List =======\n")
    print(tabulate(table, headers=["Name", "Status"], tablefmt="grid"))
    print('Patients listed successfully...!')

  def get_next_patient(self):
    if not self.queue:
        print("No patients in queue.")
        return
    patient = self.queue.pop(0)
    print(f"Next patient: {patient.name}")
    print('Retrieved successfully...!')

  def remove_patient(self, name):
    for i in range(len(self.queue)):
      if self.queue[i].name.lower() == name.lower():
        self.queue.pop(i)
        print('Patient removed successfully...!')
        return
    print('Patient not found!')


  def check_queue_capacity(self):
      print('Queue capacity:', len(self.queue))
      return len(self.queue)
'''
s=Specialization()
s.add_patient('John', 0)
s.add_patient('Jane', 1)
s.add_patient('Bob', 2)

s.list_patients()
s.get_next_patient()
s.remove_patient('Jane')
s.list_patients()
s.check_queue_capacity()
'''
