def vector_add(a, b):
	return [a_i + b_i for a_i, b_i in zip(a, b)]

def vector_sum(a):
	sum = a[0]
	for i in a[1:]:
		sum += i
	return sum

print vector_sum([1,2,3,4,5])