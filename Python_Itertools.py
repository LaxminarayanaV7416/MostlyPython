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

