# Lets see how property decorators play crucial role while using oops in python
# we have access to setter, getter and deleter methods using oops
# lets go deep and understand about them with proper examples

class EmployeeWithProperty:

    def __init__(self, first,  last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def full_name(self):
        return f'{self.first} {self.last}'
    
    def print_name_sal(self):
        return f'{self.full_name} and salary is {self.pay}'

emp1 = EmployeeWithProperty('Laxminarayana','Vadnala','500000')

print(emp1.full_name)
print(emp1.print_name_sal())