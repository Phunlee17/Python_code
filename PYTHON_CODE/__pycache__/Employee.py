class Employ:
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = first + last +'@gmail.com'
        
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay *self.raise_amt)
class Developer(Employ):
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
    
class Manager(Employ):
    def __init__(self, first, last, pay, employees= None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullName())
       
dev_1 = Developer('Mai', 'Phuong', 7000, 'Python')
dev_2 = Developer('Bao', 'My', 7500, 'Java')
  
mgr_1 = Manager('Phong','Linhh', 7000, [dev_1])

print(isinstance(mgr_1, Employ))

# baif 5: 5p:00








# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()



# print(dev_1.mail)
# print(dev_1.prog_lang)
  
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)