class Employ_1:
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
    def __repr__(self):
        return "Employ_1('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    def __str__(self):
        return '{} -{}'.format(self.fullName, self.mail)
    
emp_1 = Employ_1('Mai', 'Phuong', 7000)
emp_2 = Employ_1('Bao', 'My', 7500)

# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())