# funcools is the builtin module in python
# it has some powerful tools buitlin when we are dealing with functions and methods

# lets start functools by importing functools module as func
import functools as func

#lets start working around the reduce method first which will try to reduce the iterable
# consider we want to find sum of elements in list where we can use reduce
# note function your going to provide in reduce should consume previous element and current element
# lets see some simple example
red = func.reduce(lambda x,y:x+y , [1,2,3,4,5]) #syntax (function(previous,currrent), list or iterable you want to reduce, intialiser)
print(red)
#lets see one example with intializer in reduce 
#intializer is nothing but the intial value to start off or providing previous value in function in starting phase of execution
red = func.reduce(lambda x,y:x+y, [1,2,3,4,5], 10) # so it will start with 10+1 => 11+2 => 13+3 ..
print(red)

#############################################################
#############################################################


#lets talk about total_ordering from functools
# total_ordering is a decortor over a class which will fill up the lessthan equal, equal, greater tham equal conditions
# which are usually defined by dunder methods like __eq__ for equal too, __le__ for less than equal to, etc
# but total_ordering requires atleast two methods to be written on being __eq__ method and other is choice of __le__,__ge__,etc

@func.total_ordering
class N: 
    def __init__(self, value): 
        self.value = value 
    def __eq__(self, other): 
        return self.value == other.value 
  
    # Reverse the function of  
    # '<' operator and accordingly 
    # other rich comparison operators 
    # due to total_ordering decorator 
    def __lt__(self, other): 
        return self.value > other.value 
  
  
print('6 > 2 :', N(6)>N(2)) 
print('3 < 1 :', N(3)<N(1)) 
print('2 <= 7 :', N(2)<= N(7)) 
print('9 >= 10 :', N(9)>= N(10)) 
print('5 == 5 :', N(5)== N(5)) 

#############################################################
#############################################################

#lets talk about cached_property from functools
# its extension of property decorator but caches he value once executed and when ever we recall it gives output from cache
# lets see simple example of cached_property

#NOTE it works only in 3.8+ version of python
'''
class Test:
    def __init__(self,hello):
        self.hello = hello

    @property
    def normal_property(self):
        print('Hello am normal property method')
        return 'normal property'

    # New in version 3.8.
    @func.cached_property
    def cache_prop(self):
        print('its similar to above but value is cached and i will be printed once!')
        return 'cached property'
'''

#############################################################
#############################################################

# now lets talk about partial function executor in python from functools
# lets see the use of it
# lets define a function 
def partial_test_with_args(arg_1, arg_2, arg_3):
    print(f'Hi all am printing all the arguents passed {arg_1} {arg_2} {arg_3}')
# now lets execute the function partial
partial_func = func.partial(partial_test_with_args, 'World' ,arg_3 = 'hello') # world will be part of the arg_1 since it is first in order
 
# now we can print the output by passing two more args to newly created partial function
partial_func(arg_2 = 'hi')#, arg_1 = 'everyone,')
# we can even get the information of function arguments and keywords from partial funcusing methods like func, keywords, args
print(partial_func.func)
print(partial_func.args)
print(partial_func.keywords)

#############################################################
#############################################################


# as we have seen the only arguments part of the code lets see the keyword argument example as well
def partial_test_with_kwargs(arg_1, kwarg_1 = 'hello'):
    print(f'{arg_1} now lets print the kwargs {kwarg_1}')

partial_func_kwarg = func.partial(partial_test_with_kwargs,kwarg_1='world')
partial_func_kwarg(arg_1 = 'Hello')


#############################################################
#############################################################

# as we have seem alot of examples and usefulness of functools till now lets use the partialmethod for defining the partial methods in classes
# these partial methods are similar to the partial functions but methods are part of the classes

class Demo: 
	def __init__(self): 
		self.color = 'black'
	def _color(self, type): 
		self.color = type

	set_red = func.partialmethod(_color, type ='red') 
	set_blue = func.partialmethod(_color, type ='blue') 
	set_green = func.partialmethod(_color, type ='green') 


obj = Demo() 
print(obj.color) 
obj.set_blue() 
print(obj.color) 

#############################################################
#############################################################


# lets talk about the reduce from functools
# this we have already covered as part of lambda functions
# lets implement min and max using reduce
list_1 = list(range(10))
# lets find the minimum of the number
minimum = func.reduce(lambda x,y: x if x < y else y, list_1)
print(minimum) # output is 0

list_2 = list_1.copy()
maximum = func.reduce(lambda x,y: x if x>y else y, list_2)
print(maximum) # output is 9

# reduce even consumes a starting values lets see an example by giving start value
list_3 = list_1.copy()
maximum = func.reduce(lambda x,y: x if x>y else y, list_3, 100)
print(maximum) # output is 100

#############################################################
#############################################################

# now lets see the update_wrapper function and how its implemented
# update_wrapper basically updates the new function which is created from the partial method from from functools
# lets see an example of the update wrapper utility
def test(a,b):
    '''this function return a+b'''
    return a+b

new_partial = func.partial(test, b=10)
new_partial.__name__ = 'new_partial'
new_partial.__doc__ = '''sum of a plus 10'''

print('Before updating wrapper')
print(new_partial.__name__)
print(new_partial.__doc__)
# now lets update the wrapper
func.update_wrapper(new_partial, test)
print('After upate wrapper')
print(new_partial.__name__)
print(new_partial.__doc__)

#############################################################
#############################################################

# as we all dealt with decorators in python now lets see how to create a decorator using wraps from fucntools
# this wrpas is used to maintain the same documentation and implementation of updated_wraps but as a decorator
def test_decorator(input_function):

    @func.wraps(input_function)
    def inner_function(*args, **kwargs):
        '''Inner function docs'''
        out = input_function(*args, **kwargs)
        return f'Lets decorate this {out}'
    print('lets see documentation of the inner fucntion {}'.format(inner_function.__doc__))
    return inner_function
# we have our decorator ready lets see it in action!!
@test_decorator
def test_test(arg_1):
    '''This is a test test function wrote to test the decorator created from wraps of functools'''
    return arg_1

print(test_test('HELLO WORLD, I LOVE JAVA ALOT'))
print(test_test.__name__)
print(test_test.__doc__)

#############################################################
#############################################################

# LRU CACHE
# LRU_cache is a function decorator used for saving up to the maxsize most recent calls of a function. 
# This can save time and memory in case of repeated calls with the same arguments.
# If *maxsize* is set to None, the cache can grow without bound. If *typed* is True, 
# arguments of different data types will be cached separately. For example, f(1.0) and f(1) will be memoized distinctly.


@func.lru_cache(maxsize = None,typed=False) 
def factorial(n): 
	if n<= 1: 
		return 1
	return n * factorial(n-1) 
print([factorial(n) for n in range(7)])
print(factorial.cache_info()) 

#############################################################
#############################################################

# It is a function decorator. It transforms a function into a generic function so that it can have different behaviors 
# depending upon the type of its first argument. It is used for function overloading,
# the overloaded implementations are registered using the register() attribute of the

@func.singledispatch
def fun(s): 
	print(s) 
@fun.register(int) 
def _(s): 
	print(s * 2) 
@fun.register 
def _(s:list): 
	print(sum(s))

fun('GeeksforGeeks') 
fun(10) 
fun(list(range(10)))

