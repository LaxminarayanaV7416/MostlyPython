# itertools is the builtin module in python
# it has some powerful tools buitlin when we are dealing with iterators

import itertools

# lets start looking into count 
sample_counter = itertools.count()
# so to enable counter we can use next(sample_counter) to get count
print(next(sample_counter))
print(next(sample_counter))

# lets see an example of how to enable a counter
list_1 = list('ABCDEFG')
count_list = [(i,j) for i,j in zip(list_1,sample_counter)] # as we can see the iterator remembers where it left off
print(count_list)

# we can initialize the count with start and step which we will look at the example deeply
sample_counter_2 = itertools.count(start=10,step=-2.5)
print(next(sample_counter_2))
print(next(sample_counter_2))
print(next(sample_counter_2))
print(next(sample_counter_2))

#############################################################
#############################################################

# lets talk about zip_longest method from the itertools
# lets first try to understand the difference between the zip and zip_longest
# zip when we zip two iterables together it will generate a iterator where it will try to see the minimum length and from the two iterables 
# and the iterator generated will be on minimum length. fro e.g if we have list_1 with length 10 and list_2 with length 20
# when we zip list_1 and list_2 we will iterator of length 10.

# how zip_longest helpful is to minimize this condition and now wen zip_longest the list_1 and list_2 we will get iterator of length 20
# where as the remaining values of the list_1 will be None /or we can use fillvalue = None(default), fillvalue='Something'

sample_list = [(i,j) for i,j in zip(range(10),list('ABCDE'))]
print(sample_list)
longest_list = [(i,j) for i,j in itertools.zip_longest(range(10),list('ABCDE'),fillvalue='Lucky')] # note by default fillvalue = None
print(longest_list)

#############################################################
#############################################################

# Now lets talk about cycle from itertools it is similar to count but here the values are predefined and it will cycle through them
# lets see an example to understand
sample_cycle = itertools.cycle(['ON','OFF'])
cycle_list = [(i,j) for i,j in zip(sample_cycle, list('ABCDEF'))]
print(cycle_list)

#############################################################
#############################################################

# itertools repeat is one of the most useful method where we can repeat

sample_repeat = itertools.repeat('Lucky',times=5) # without times keyword it is an infifnite loop
for i in sample_repeat:
    print(i)

squares = list(map(pow, range(10), itertools.repeat(2))) # note map can use consume multiple iterables after a function
print(squares)

#############################################################
#############################################################

# map is a builtin method in python which will consume function and many iterables so that every iterables value per once
# will be mapped to the function and output is saved as iterator.

# what if we have an iterable which has tuple of pairs for instance [(1,2,3),(4,5,6)] =, we can use this with map 
# as well as starmap from itertools.

count = itertools.repeat(3)
x = [i for i in zip(range(1,11),count)]
y = list(itertools.starmap(pow, x))
print(y)

#############################################################
#############################################################

# Lets talk about permutations in itertools
# little intriduction about permutations all different ways to group item where the order DOES matter.

letters = ['a','b','c','d']
numbers = [0,1,2,3]
names = ['lucky','lax','laxminarayana']

result = itertools.permutations(letters,2)

#remember the Order do matter!!
for i in result:
    print(i) 
print('-------------')    

#############################################################
#############################################################

# Lets talk about Combinations in itertools
# little intriduction about Combinations all different ways to group item where the order DOES NOT matter.

letters = ['a','b','c','d']
numbers = [0,1,2,3]
names = ['lucky','lax','laxminarayana']

result = itertools.combinations(letters,2)

#remember the Order do not matter!!
for i in result:
    print(i) 
print('-------------')    


# there is one more way to allow repeat values in combinations that is combinations_with_replacement
result = itertools.combinations_with_replacement(letters,4)

#remember the Order do not matter!!
for i in result:
    print(i) 
print('-------------')    
#############################################################
#############################################################

# lets see the cartisean product of the iterables which will be able to get the same kinda types for
# isntance we want a number of 4 and all possible permutations where repeating a number for multiple times also do matter.
# 1111,1112, etc.,

letters = ['a','b','c','d']
numbers = [0,1,2,3]
names = ['lucky','lax','laxminarayana']

result = itertools.product(numbers,repeat=4)

for i in result:
    print(i)
print('-------------')    

#############################################################
#############################################################

# lets talk about chain method in the itertools
# consider the situation where we want to extend two or more lists together and make one list.
# where this activity wouldnt be memory efficient, so we have chain to do so

letters = ['a','b','c','d']
numbers = [0,1,2,3]

extended_list = itertools.chain(letters,numbers)

for i in extended_list:
    print(i)

#############################################################
#############################################################

# Lets see the slicing of iterators
# we can use itertools method like islice -> which means iterator slice.
# lets the use case here
# when we try to read a file it will be as TextIOWrapper which is an object and iterator by itself, but when we apply
# TextIOWrapper based methods like readlines which will convert the IOWrapper to list which may overload the memory.

# a test snippet to avoid the readlines method.
'''
with open('README.md', mode='r', encoding='utf-8') as file_opened:
    for line in file_opened:
        print(line)
'''

# now when we want to slice the iterator direclty we can do that with islice
with open('README.md', mode='r', encoding='utf-8') as file_opened:
    for line in itertools.islice(file_opened,1,10,3): # syntax is islice(iterator, stop) or islice(iterator,start,stop,step)
        print(line)

#############################################################
#############################################################

