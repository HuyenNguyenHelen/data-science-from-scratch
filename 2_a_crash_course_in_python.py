#-------------
#intro

#python should only have one way to do something. if it's right
#it's called pythonic. 


#-------
#whitespace

#python uses indentation to delimit blocks of code
#whitespace is ignored inside parentheses and brackets
long_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
					+ 9 + 10)
list_of_list = [[1, 2, 3],
				[4, 5, 6],
				[7, 8, 9]]
#you can use backslash to indicate a statement continues on the next line
#sometimes problems with pasting due to white space. if happens, use 
#%paste function.


#-------
#modules

#these are features not loaded by default
#simple -> import re
#simple with new name -> import re as regrex
#specific features without qualification -> from collections
#import defaultdict, Counter
#everything without qualification (overwrite risk)-> from re import *


#-------
#arithmetic
#default is integer divison so use float() on one argument


#-------
#functions

#functions are first class which means we can assign them to variables
#and pass them into functions like other arguments
#don't understand
def double(x):
	return x * 2

def apply_to_one(f):
	return f(1)


#easy to make anyonymous functions or lambdas
y = apply_to_one(lambda x: x + 4)

#you shouldn't assign lambdas to variables and use def instead

#default arguments
def my_print(message = "default"):
	print message


#------------------
#strings

#single or double quotes
#backlashes for special characters like "\t" for tab
#multi line strings using driple-quotes


#------------------------------
#exceptions

def exception_example():
	try:
		print 0/0
	except ZeroDivisionError:
		print "cannot divide by zero"



#------------------------------
#lists

#most fundamental data structure in python
#ordered collection
#other languages might call it array
#can be heterogenous and can make lists of lists
list = [[1,2,3],
		["a", "b", "c"]]

#sum() and len() are useful
#can select with square brackets. negative if from end.
#also inclusive on beginning and exclusive on end.
slice = list[0:2]

#list membership
#1 in [1,2,3] is true

#can extend, add, append
list.extend([4,5,6])
list2 = list + [4,5,6] #if no modify
list.append(4) #for single elements

#can unpack them
x, y = [1, 2]

#common to use underscore for things that will be deleted
_, y = [1, 2]


#------------------------------
#tuples

#lists's immutable cousin. can do everything you can do to lists that 
#doesnt involve modification
#can create with parentheses or nothing instead of square brackets

#convenient way to return multiple values from functions
def sum_and_product(x,y):
	return x + y, x * y


#------------------------------
#dictionaries

empty_dict = {}
empty_dict2 = dict()
grades = {"joel": 88, "john": 55}

#check for existence
joel_has_grade = "joel" in grades

#frequently used to repreesent structured data

#selection
tweet = {
	"age": 20,
	"user": "joel",
	"fave_numbers": [20, 30, 40]
}

keys = tweet.keys()
values = tweet.values()
items = tweet.items()


#------------------------------
#defaultdict

#like a regular dictionary except that it deals well with missing keys
#when look up key that's not in dict, first adds value for it using
#non-zero argument function

from collections import defaultdict
word_counts = defaultdict(int) #int() produces 0


#------------------------------
#Counter

#turns sequence of values into a defualdict(int)-like object
#mapping keys to counts. used for histograms. 

from collections import Counter
C = Counter([0, 1, 2, 0])

#has most_common method that is useful


#------------------------------
#Sets

#represent collections of distinct elements
s = set()
s.add(1)
s.add(1)
x = len(s)

#useful because in is very fast on sets

#also useful to find distinct elements from collection
numbers = [1,2,3,4,5,6,3,5,2]
numbers_s = set(numbers)
unique = len(numbers_s)

#not as common as lists or dics


#---------------------------------------
#Control flow

#standard structure is if, elif(s), else

#ternary statement
parity = "even" if x % 2 == 0 else "odd"

#while loop ok but usually we use for and in
#x = 0
#while x < 10:
	#do something

#for x in range(10):
	#do something

#for more complex logic, use continue and break


#---------------------------------------
#truthiness

#capitalized
#None indicates a nonexistent value and similar to null elsewhere
#instead of == use is
#falsy: False, None, [], {}, "", set(), 0, 0.0
#true: everything else

#all() function takes a list and returns true when every element
#is truthy 

#any() function return true when at leats one element is true

#--------------------------------------------
#--------------------------------------------
#not so basics


#---------------------------------------------
#sorting

x = [4, 1, 3]
y = sorted(x) #create new list
x.sort() # modify existing list
#can add reverse = True as parameter

#sort result of function specified with key
#wc = sorted(word_counts.items(),
	 #key = lambda (word, count): count, 
	 #reverse = True)


#---------------------------------------------
#list comprehensions

#pythonic way to transform lists or selecting elements from list
even_numbers = [x for x in range(5) if x % 2 == 0]
squares = [x **2 for x in range(5)]
even_squares = [x * x for x in even_numbers]

square_dict = {x: x * x for x in range(5)}

#multiple fors
pairs = [(x, y)
		 for x in range(10)
		 for y in range(10)]


#---------------------------------------------
#generators and iterators 

#lists can grow too big. if only deal 1 element at a time, inefficient.

#generators can be iterated over using for where values are produced
#as needed

#one way to create is with functions and yield
def lazy_range(n):
	#lazy version of range
	i = 0
	while i < n:
		yield i
		i += 1

#this consumes yielded values one at a time until they're gone
#for i in lazy_range(10):
	#do_something_with(i)

#in python 3 range() is laxy and before xrange() is lazy
#downside of generators is you can only iterate through once

#other way create generators is comprehensions wrapped in parentheses
#lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

#every dict has items() that returns key-value pairs

#we more frequently use iteritems() which lazily yields key-value pairs
#one at at time


#---------------------------------------------
#randomness 

import random
four_uniform_randoms = [random.random() for _ in range(4)]

#random module is deterministic 

#you can change internal state with random.seed for reproducible
#results
random.seed(18) #now random.random() will get same numbers

#random.randrage() takes 2 arguments and returns element from range
#random.shuffle() randomly reorders elements of a list

#random.choice() randomly picks element from list
best_friend = random.choice(["john", "jason", "ellen"])

#choose sample without replacement with use random.sample()
#choose sample with replacement use multiple random.choice()


#---------------------------------------------
#regular expressions

#provide way of searching text 


#---------------------------------------------
#OOP

#make own set class
#want to add items, remove items, and check if x value is contained
#all function will be member functions (dot after object)
class Set:
	def __init__(self, values = None):
		#this is the constructor 
		self.dict = {} #each instance has dict property
		if values is not None:
			for value in values:
				self.add(value)

	def __repr__(self):
		#this is string repr of set object
		return "Set: " + str(self.dict.keys())

	def add(self, value):
		self.dict[value] = True

	def contains(self, value):
		return value in self.dict

	def remove(self, value):
		del self.dict[value]



#---------------------------------------------
#functional tools

#sometimes want to partially apply or curry functions to 
#create new functions
def exp(base, power):
	return base ** power

def two_to_the(power):
	return exp(2, power)

#better approach
from functools import partial
two_to_the = partial(exp, 2)

#can also use partial to fill later arguements if you fill names
square_of = partial(exp, power = 2)
#print square_of(3)

#also use map(), reduce(), and filter() for functional alternatives
#to list comprehensions
def double(x):
	return 2 * x
xs = [1, 2, 3, 4]
twice_xs = [double(xs) for x in xs]  #[2, 4, 6, 8]
twice_xs = map(double, xs) #same as above
list_doubler = partial(map, double) #function that doubles a list
twice_xs = list_doubler(xs) #again [2, 4, 6, 8]

#map with multiple-argument functions if multiple lists
def multiply(x, y): return x * y
products = map(multiply, [1,2], [4,5]) #[4, 10]

#similarly, filter does work of list comprehension if
def is_even(x):
	return x % 2 == 0
x_evens = [x for x in xs if is_even(x)] #[2, 4]
x_evens = filter(is_even, xs) #same as above
list_evener = partial(filter, is_even) #function that filters a list
x_evens = list_evener(xs) #again [2,4]

#and reduce() combines first two elements, that with third, etc.
x_product = reduce(multiply, xs) #24
list_product = partial(reduce, multiply) #function that reduces list
x_product = list_product(xs) #again 24


#---------------------------------------------
#enumerate

#sometimes want iterate on list want index and element
#this is very common
#pythonic solution is enumerate which produces tuples (index, element)
list = ["john", "adam", "jack"]
#for i, name in enumerate(list):
	#do something with i or name

#if just want index
#for i, _ in enumerate(list):
	#do shit


#---------------------------------------------
#zip and argument unpacking

#zip transforms multiple lists into a single list of types of 
#corresponding elements

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
lists = zip(list1, list2)

#unzip with this odd trick
letters, numbers = zip(*lists) #asterisk perform argument unpacking


#---------------------------------------------
#args and kwargs

#create high-order function that takes input function f and returns
#new function that returns twice value of f
def doubler(f):
	def g(x):
		return 2 * f(x)
	return g

#this works in some cases but breaks down with 2+ argument functions
def f1(x):
	return x + 1

g = doubler(f1)
#can print g(3) -> 8 ((3+1) * 2)

#need way to specify function that takes arbitrary n arguments
def magic(*args, **kwargs):
	print "unnamed args:", args
	print "keyword args:", kwargs

#magic(1,2, key="word", key2= "word2") returns tuple(1, 2) 
#as named arguments and a dict with {'key': 'word', 
#'key2': 'word2'} 

#you can also do other way around
def other_way_magic(x, y, z):
	return x + y + z
x_y_list = [1, 2]
z_dict = {"z": 3}
print other_way_magic(*x_y_list, **z_dict)

#can do many tricks. we will use to producer high-order functions
#that accept arbitrary arguments


#-------
#further exploration

#official python tutorial
#python for data analysis by we mckinney


