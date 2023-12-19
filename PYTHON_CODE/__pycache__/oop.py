class Employee: 
  
    num_of_emps=0
    raise_mount = 1.04
  
    def __init__(self, firstName, lastName, pay):
      self.firstName = firstName
      self.lastName = lastName
      self.pay = pay
      self.email = firstName + lastName + '@gmail.com'
      
      Employee.num_of_emps +=1
      
    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)
      
    def apply_raise(self):
      self.pay = int(self.pay *self.raise_mount)
      
    @classmethod
    def set_raise_amount(cls, amount):
      cls.raise_mount = amount
      
    @classmethod
    def from_string(cls, emp_str):
      firstName, lastName, pay = emp_str.split('-')
      
      return cls(firstName, lastName, pay)
    
    @staticmethod
    def is_workday(day):
      if day.weekday() ==5 or day.weekday()==6:
        return False
      return True
      
emp1 = Employee('Phuong', 'Le', 5000)
emp2 = Employee('Bao' , 'My' , 6000)

import datetime
my_date = datetime.date(2023, 12, 11)
print(Employee.is_workday(my_date))
# emp1.set_raise_amount(1.05)
# print(Employee.num_of_emps)

# print(Employee.raise_mount)
# print(emp1.raise_mount)
# print(emp2.raise_mount)

# emp_str_1 = 'Di-Kien-1500'
# emp_str_2 = 'Mai-Phuong-2000'
# emp_str_3 = 'Phong-Linh-1998'

# # firstName, lastName, pay = emp_str_1.split('-')

# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)