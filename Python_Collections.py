# lets talk about Python's Most widely used inbuilt module collections
# Collections is nothing but the container datatypes, whcih are very handy and faster
# we will talk about five main aspects in collections counter, ordereddict, namedtuple, defaultdict, deque

#please refer documenattion for object oriened benfits of UserList, UserString which can be used in OOPS



# Let's Start by importing python collections
import collections as clct 

#lets start this lesson with counter 
sample_str = 'aaabbbbbbbxxccx'
count = clct.Counter(sample_str)

#count is a dictionary so we can use the .items, .keys, .value methods to get what ever we are intrested
print(count) # outputs as dictionary output is Counter({'b': 7, 'a': 3, 'x': 3, 'c': 2})
print(count.most_common(3)) #outputs the most common elements as list for eg. [('a', 5), ('b', 4), ('c', 3)]
print(list(count.elements())) #to see all the elements and by default it gives iterables so am converting it to list

#############################################################
#############################################################

# Now lets talk about the namedtuple, its a lightweight object type similar to struct
# lets make a named tuple its quite simple 
# syntax to for named tuple is we are creating a class called Tup-class and passing the same as first argument, and second argument
# is values as string but comma seperated as shown below
Tup_class = clct.namedtuple('Tup_class','ele1,ele2,ele3,ele4') 
tup = Tup_class('all of','us','love','python') #hurrey we have created the namedtuple and instantiated the class
print(tup) # we are directly printing the named tuple
print(tup.ele1) # we can access individual elements by calling with there respective names
#lets see other benfits of using named tuple
sample_list = ['my name','is what',15000,'something happend']
tup2 = Tup_class._make(sample_list)
print(tup2)
#lets convert named tuple to dictionary
print(tup2._asdict()) #this will convert to ordereddict object and we can use it as noraml dictionary as well.


#############################################################
#############################################################


# Now lets see about the OrderedDict 
# ordereddict is dictionary which will remember the order as we pass the keys and values
ord_dict = clct.OrderedDict()
ord_dict['hello']=58660
ord_dict['world']=20419
# dictionary remebers the order 
print(ord_dict.keys())

#############################################################
#############################################################

# Now lets talk about defaultdict
# default dict is used to when we want to set default value when key doesnot exists (to avoid KeyError)
def_dict = clct.defaultdict(list) # i have set the empty list as default value if we dont passs anything its none
# we have to pass explicity list,set,dict,tuple,int,float,str
def_dict['world']=1235
print(def_dict['world'],def_dict['lucky']) # as key lucky doesnt exists it prints empty list


#############################################################
#############################################################

# now lets learn about deque -> its nothing but the listwith some extra benifits of adding to left most place , removing left etc
deq = clct.deque([1,2,3]) # converted a normal list to deque for extra benfits
deq.appendleft(4) #appends element 4 in the first place that is left most position or zero index
deq.extendleft([5,6]) # extends left but we will ass the last element as first
deq.popleft() #removes the first element from the list

#############################################################
#############################################################