#-------------------------------------------------------------------------
#intro

#linear algebra deals with vector spaces


#-------------------------------------------------------------------------
#vectors

#vectors are objects that can be added together (make new vectors)
#or multiplied by scalars (new vectors)

#vectors are points in some finite-dimensional space

#if you have heighs, weights, and ages for people you can treat 
#data as 3-dimensional vectors (height, weight, age)

height_weight_age = [70, 170, 40]

#we want to do arithmetic on vectors but python lists aren't vectors
#so we have to build these tools ourselves

#vectors add componentwise
#we can implement by zip-ing and using list comprehension

def vector_add(a, b):
	return [a_i + b_i for a_i, b_i in zip(a, b)]

def vector_subtract(a, b):
	return [a_i - b_i for a_i, b_i in zip(a, b)]

def vector_sum(vectors):
	result = vectors[0]
	for vector in vectors[1:]:
		result = vector_add(result, vector)
	return result 

#other way
def vector_sum(vectors):
	return reduce(vector_add, vectors)

#another way
from functools import partial
vector_sum = partial(reduce, vector_add) #more clever than helpful

#scalar multiply
def scalar_multiply(c, v):
	return [c * v_i for v_i in v]

#vector mean is comonentwise mean of same-sized vector list
def vector_mean(vectors):
	n = len(vectors)
	return scalar_multiply(1/n, vector_sum(vectors))

#dot product is sum of componentwise  products
def dot(a, b):
	return sum([a_i * b_i for a_i, b_i in zip(a, b)])

#dot product measures how far vector a extends in b directions
#if b = [1,0], dot(a,b) is first component of a
#dot product is length of vector if you project a onto b

def sum_of_squares(a):
	return dot(a, a)

import math
def magnitude(a):
	return math.sqrt(sum_of_squares(a))

def squared_distance(a, b):
	return sum_of_squares(vector_subtract(a, b))

def distance(a, b):
	return math.sqrt(vector_subtract(a, b))

def distance(a, b):
	return magnitude(vector_subtract(a, b))

#using lists as vectors is good for exposition but terrible for
#performance

#in production code would use NumPy library which includes high
#performance array class with many included operations


#-------------------------------------------------------------------------
#matrices

#matrix is a 2-dimension collection of numbers represented
#as lists of lists

#matrix A where A[i][j] is element in ith row and jth column
#we use capitals to represent matrices

#rows = len(A) and columns = len(A[0])
def shape(A):
	num_rows = len(A)
	num_cols = len(A[0]) if A else 0
	return num_rows, num_cols

#nxk matrix has n rows and k columns

def get_row(A, i):
	return A[i]

def get_column(A, j):
	return [A_i[j] for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
	return [[entry_fn(i, j)
	         for j in range(num_cols)]
	         for i in range(num_rows)]

def is_diagonal(i, j):
	return 1 if i == j else 0

#identity_matrix = make_matrix(5, 5, is_diagonal)

#matrix important because can represent data set consisting of multiple
#rows. if you had 100 ppl with age and height, could make 100x2 matrix

#also useful because can use nxk matrix to represent linear function
#that maps k-dimensional vectors to n-dimensional vectors

#third, matrices can represent binary relationships well
#with frienships instead of friends = [(0,1), (2,0), etc.] can do
# friends = [[0,1,1,0,1], [1,0,1,1,0], etc.]. faster for lookups


#-------------------------------------------------------------------------
#further exploration

#linear algebra from uc davis
#linear algebra from saint michael's college
#linear algebra done wrong
#NumPy

#you can prove pythagoreas theorem by drawing a square and fitting a 
#square inside at an angle. on each side you have a and b (the amount
#by which the inside rectangle is turned. the square on the inside
#has all sides equal to c. now you can solve for the size of the whole
#thing with 2 equations and arrive at the theorem.)