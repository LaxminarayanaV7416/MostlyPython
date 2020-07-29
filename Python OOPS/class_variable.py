# Lets talk about the differenece between class variables and instance variables
# Class Variables ==> Class variables are respective to single class and if we try to change a class varibale with
# it will be changed accross the class i.e., across all the instances which class have defined
# Instance variables ==> Instance variales are with respectto instacne, if we do any changes to the instance of class 
# the result will be with in the instacne of the class only.

class Employee: #lets create a class

    raise_amount = 1.10 #this is the class variable
    # print(Employee.__dict__) to see the class varible in that

    def __init__(self, first,  last, pay):
        self.first = first # this is called instance variable
        self.last = last
        self.pay = pay

    def full_name(self):
        return f'{self.first} {self.last}'

    # we can modify class variables and use them in two ways one way is below
    def increase_salary(self,amount):
        Employee.raise_amount = amount #Note here we are using the Employee which means class variable.
        return self
    
    # Another way to use class variables is by self only
    def increase_salary_2(self, amount):
        self.raise_amount = amount 
        return self
    
    @classmethod
    def increase_raise(cls,amount):
        cls.raise_amount = amount

#lets talk about the difference between both
emp1 = Employee('Laxminarayana','Vadnala',500000)
emp2 = Employee('Samanvitha', 'Sunkari', 500000)

# this is just to see how we can print the variables availablity in classes
print(Employee.__dict__) #Checking
print(emp1.__dict__)
print(emp2.__dict__)

# lets increase the salary
emp1.increase_salary(1.2) #increased using class name directly so have wider effect not only one instance ie emp1
print('After increase using Class Name directly',emp1.__dict__)
print('Lets see emp2 dict',emp2.__dict__)
print(Employee.__dict__)

emp1 = Employee('Laxminarayana','Vadnala',500000)
emp2 = Employee('Samanvitha', 'Sunkari', 500000)

#now we are increasing with self so it has effect only on emp1 that is insttance alone
emp1.increase_salary_2(1.3) 
print('After increasing using instance variable that is self==>',emp1.__dict__)
print('Lets see emp2 dict',emp2.__dict__)
print(Employee.__dict__)

#If you have noticed we have a new instance varible inside the dict thats how we are trying to convert
# class variable to instance variable (this is not exactly conversion but we are briging down the scope)
# Scope of varibles and search policy in OOPS
# Instance varibles(self) => Class variables (cls) => Global varibles (wrt program)
# lets see same example different way

emp1 = Employee('Laxminarayana','Vadnala',500000)
emp2 = Employee('Samanvitha', 'Sunkari', 500000)

# ALtering the class by class name directly if we try to change 
Employee.raise_amount = 1.4
#======== (OR) ========#
emp1.increase_raise(1.4) #lets talk more about using classmethods while discussing about them

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

#NOTE - if you have observed clearly when ever we are trying to change the class varible 
# with the help of the class name directly its affecting the all the instances so this is so capability of class varibles

#now let me change the value in using the instance variable
# Yes we can change class varibles wrt to isntances
emp1 = Employee('Laxminarayana','Vadnala',500000)
emp2 = Employee('Samanvitha', 'Sunkari', 500000)

print(emp1.raise_amount)
emp1.raise_amount = 1.5

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# so from converntion for class varibles we can either use self or cls

#=================================#
# Now lets talk about the class methods and static methods
# CLASS METHODS -> Which can use class varibles and they are mainly used to create 
# another instance of the classes lets walk through of an example

class Parent:

    fam_cunt = 0 # lets define a new class varible 

    def __init__(self, childs):
        self.childs = childs
        # we can use class varibles as refernece becaz there details are present in all the insatcnes
        Parent.fam_cunt += 1

    @classmethod
    def child_to_parent(cls,children_born):
        # when childs grows up and have kids ultimately he is also a parent
        return Parent(children_born)

fam1 = Parent(2)
# now we are trying to create new isnatcne of parent class from exisiting instance
fam2 = fam1.child_to_parent(1)

print(fam1.__dict__)
print(fam2.__dict__)
print(Parent.fam_cunt) #isnt it cool class variables are like a central database for all instances of classes

# Now lets talk about the static methods 
# STATIC METHODS -> static methods are one which doesnt use any self or cls (in other words no isnatnce is refered)
# static methods are just like the normal functions but they are grouped with class becaz they are some how related to them.

class Family:

    def __init__(self,members):
        self.members = members

    @staticmethod
    def is_enjoying(trips):
        # this methods tells whether family is enjoying or not based on number of trips done by family
        if trips >= 2:
            return True
        return False

fam = Family(3)
print(fam.is_enjoying(3))
print(fam.is_enjoying(1))