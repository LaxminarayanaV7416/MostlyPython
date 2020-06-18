# classes are used to logically group data together
# every class in python is inherited from object
# function inside classes or associated with class are called as methods
# varibles used inside classes which will be defined as self is known as variables
# we will be defining classes and learning oops based on strict python syntax using typing package.

import typing

''' Most used python typing classes are 
   List, Tuple, Dict, Set, int, float, str, Sequence, NewType, Mapping, Callable, Iterable,  
'''

# A sample test class which doesnt accept any attributes
class Employee:
   pass

#lets create an instace for our class
emp1 = Employee()
# we can manually assign what attribute we need to the instance
emp1.first = 'Laxminarayana'
emp1.last = 'Vadnala'
#print to test it hurrey! it works
print(emp1.first)

#lets try iwth other instance
emp2 = Employee()
emp2.first = 'Laxminarayana'
emp2.last = 'Vadnala'

#print to see they are completely different from each other
#hurrey our OOPS Journey is wonderful!
print(emp1)
print(emp2)

#now we have seen how classes are useful
#lets create a class with constructor which accepts attributes
class EmployeeTwo(object):

   def __init__(self,first,last,salary):
      self.first = first
      self.namelast = last #we can assign what every attribute name we want
      #but remember if we want to use attribute last we need to use
      #self.namelast attribute inside thee class methods which consumes self
      self.salary = salary

   def fullname(self): # our first method wrote inside the class
      return f'{self.first} {self.namelast}'

emp1 = EmployeeTwo('Laxminarayana','Vadnala',500000)
print(emp1.fullname()) # look we have provided the self as argument in defination of our method
#what ever we called above will be converted to call like below
print(EmployeeTwo.fullname(emp1)) # this he reason we are trying to give self

'''
As of now we have worked on classes creation 
basics lets see basics in advanced mode ON
which basically means in for of 
static typing'''
#lets create the class with static typing

class EmployeeThree(object):

   first :  str
   last : str
   salary : float

   def __init__(self,first : str, last : str, salary : float) -> None:
      self.first = first
      self.last = last
      self.salary = salary

   def salary_increaser(self, percent : float) -> float:
      return self.salary*(100 + percent)

#lets see more advanced way to implemet oops in static typing
from dataclasses import dataclass

@dataclass
class EmployeeFour:
   first : str
   last : str
   salary : float = 600000

   ''' As we have used dataclass which will automatically create the constructor for us by mentioning above things
   def __init__(self,first : str, last : str, salary : float = 600000) -> None:
      self.first = first
      self.last = last
      self.salary = salary
   this looks we are alnost there on basics get stronger on static typing for betterment on python
   '''

   def fullname(self):
      return f'{self.first} {self.last}' #we can use the same attribute with self inffront better asscess
