# lets talk about lambda functions in this file.

# lambda functions are called as functions without a name / miscellenoeus functions without a def keyword (usually lambda functions
# are written one line)

# basic syntax of lambda functions is --> lambda arguments : expression
# lets see some basic examples of lambda functions

example_1 = lambda arg_1 : arg_1 ** 3 # a simple lambda function returns the cube of the number
print(example_1(5)) # execution of lambda function returns 125

example_2 = lambda arg_1, arg_2 : arg_1 ** arg_2 # simple function returns the arg+1 to the power of arg_2
print(example_2(5,3)) # execution of lambda function returns 125

#############################################################
#############################################################

# we can use lambda function with filter(), map() and reduce()
# where these are the builtin functions which consume the function adn iterable(list,tuple,string) and returns the genrator object

# lets see some examples of how filter is useful
# filter is used to filter out the opeartions.
list_1 = list(range(20)) # have a list from 0-19 where i wanted to find the even numbers and get it as a separate list
even_list = list(filter(lambda arg_1 : arg_1 % 2 == 0, list_1)) # simple filetr function 
print(even_list) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#############################################################
#############################################################

# now lets see some examples of map and how it is useful
# map is used for iterator transformations and syntax for map is same as 
list_2 = list(range(20))
square_list = list(map(lambda arg_1 : arg_1 ** 2, list_2))
print(square_list) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]

#############################################################
#############################################################

# as in new version reduce is moved from bultin fucntions to functools
# lets import the reduce from functools
from functools import reduce

# lets see some examples of the reduce using lambda expressions
# reduce syntax -> reduce(function, iterator, initial value)
list_3 = list(range(10))
test = reduce(lambda arg_1,arg_2 : arg_1+arg_2,list_3) # simple replacement of sum 
print(test) # 45


#############################################################
#############################################################

# now we have covered the lambda expressions and they are so much useful
# lets see some complex code for lamda expressions

# lambda expressions with if and else statements
# lambda <arguments> : <Return Value if condition is True> if <condition> else <Return Value if condition is False>
# lets see and example
# Note wanted to return a list where is number is <= 10 (then square) else (cube it)
list_4 = list(range(20))
if_else_lambda = list(map(lambda arg_1 : arg_1 ** 2 if arg_1 <= 10 else arg_1 ** 3, list_4))
print(if_else_lambda) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]

#############################################################
#############################################################

# lambda expressions with if elif and else statements
# lambda <args> : <return Value> if <condition > ( <return value > if <condition> else <return value>)
# same example as above but we have if numb <= 5 (square it), numb <= 10 (cube it ) else (power 4 it)
list_5 = list(range(20))
if_elif_else_lambda = list(map(lambda arg_1 : arg_1 ** 2 if arg_1 <= 5  else (arg_1 ** 3 if (arg_1 <=10 and arg_1 > 5) else arg_1 ** 4), list_5))
print(if_elif_else_lambda) # [0, 1, 4, 9, 16, 25, 216, 343, 512, 729, 1000, 14641, 20736, 28561, 38416, 50625, 65536, 83521, 104976, 130321]
