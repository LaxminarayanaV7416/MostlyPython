# lets talk about inheritance what are the benfits of inheritance
# Inheritance means getting all the methods and varibles defined in onee class to another
# class which we are inheriting to. more over we can customise the inherited variables and methods 
# in the child class

#lets also talk about types of inheritance in general
# 1. Single inheritance

#lets walk through single inheritance example

class Parent:
    
    def __init__(self,father_name,mother_name):
        self.father_name = father_name
        self.mother_name = mother_name

    def child_born(self,hospital):
        text = f'Congratulations!! your child is jr.{self.father_name} born in {hospital}'
        return text

class ChildParent(Parent):
    pass

test_fam = ChildParent('Testing Father', 'Testing Mother')
print(test_fam.child_born('Sun Shine Hospital'))
print(test_fam.__class__)

#As you have noticed above we have a powerful tool called inheritance we can customise this as of our need
# lets see all these aspects in later examples

# lets see single inheritance with advanced super keyword use

class HumanBeing:

    def __init__(self,dob):
        self.dob = dob

    def sick_decider(self,temperature):
        if temperature >= 98.5:
            return 'Sick!!'
        return 'Healthy!!'

class Father(HumanBeing):
    
    def __init__(self,dob,name):
        super(Father,self).__init__(dob)
        self.name = name

# super(className, self) where in method resolution order it starts searching from the point you meentioed classname

being = Father('2111997','Lucky')
print(being.sick_decider(97.3))


# lets see inheritance using super keyword
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

#=============(OR)===========#
class Square_2(Rectangle):

    def __init__(self,length):
        Rectangle.__init__(self,length,length)

# NOTE : The main important note of thee superkey word is simple 
# consider teh example, we are dealing with classes with name A,B,C,D
# A is parent, B is also parent, C inherits A,B at once
# so now we are in problem that we have a concept called method resolution order which can be looked when we use
# (C.__mro__) => we can see that when we try to access any methods instance gonna look and follows MRO which is like
# first looks in C if not defined looks in A (as class C(A,B)) then lastly looks in B.

#Best point is we can rewrite the methods or attributes we want by specifying the ClassName.methodsname(self,*args)
# BUT its as part of code maintainability its not the correct way so we can rewrite it as super().methodname(*args)
# when we are trying to use super remeber few important things
# ### when super is empty like super() == super(C,self), most important thing is read carefully as below
######### wanna set attributes to C class set it with self
######### wanna edit methods or changes attributes of A class use super().methodname(*args) == super(C,self).methodname(*args)
#         => super().methodname(*args) == super(C,self).methodname(*args) == A.methodname(self,*args)
######### wanna edit methods or changes attributes of B class use super(A,self).methodname(*args)
#         => super(A,self).methodname(*args) == B.methodname(self,*args)
# NOTE : There wont exists any =thing like super(B,self)... because we have understood it clearly how backreference super is taking.

# lets see the multiple inheritance example
class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last

class Assosciate:

    def __init__(self,pay):
        self.pay = pay

class SoftwareEngineer(Employee,Assosciate):

    def __init__(self,first,last,pay):
        super(SoftwareEngineer,self).__init__(first,last)
        super(Employee,self).__init__(pay)

# Please refer links mentioned in refrence formore types of inheritance