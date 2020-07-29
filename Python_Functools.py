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


#lets talk about total_ordering from functools
# total_ordering is a decortor over a class which will fill up the lessthan equal, equal, greater tham equal conditions
# which are usually defined by dunder methods like __eq__ for equal too, __le__ for less than equal to, etc
# but total_ordering requires atleast two methods to be written on being __eq__ method and other is choice of __le__,__ge__,etc

##############material pending!



#lets talk about cached_property from functools
# its extension of property decorator but caches he value once executed and when ever we recall it gives output from cache
# lets see simple example of cached_property
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


