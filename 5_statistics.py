from collections import Counter
import matplotlib.pyplot as plt
import math

#---------------------------------------------
#intro

#stats is math and techniques used to understand data


#---------------------------------------------
#describing a single set of data

#data itself might be the best description for a tiny dataset
#when data gets larger use statistics

num_friends = [100, 100, 85, 74, 120, 132, 84, 84, 0, 0, 0]

#one approach could be to make a histogram using plt.bar()
#friend_counts = Counter(num_friends)
#xs = range(200)
#ys = [friend_counts[x] for x in xs]
#plt.bar(xs, ys)
#plt.show()

#simple stats
num_points = len(num_friends)
largets_value = max(num_friends)
smallest_value = min(num_friends)
smallest_value = sorted(num_friends)[0] #same thing


#central tendencies

#mean tells you the average value in a set. it loses significance
#if there are major outliers.

def mean(x):
	return sum(x) / (len(x))


#median is the middle-most value. it doesn't depend on every value 
#in the dataset.
def median(x): #better to define midpoint and len(x) before if/else logic
	numbers = sorted(x)
	if len(x) % 2 != 0:
		return numbers[len(numbers) / 2]
	else:
		n1 = numbers[(len(numbers) / 2) - 1]
		n2 = numbers[(len(numbers) / 2)]
		return mean([n1, n2])


#a generalization of median is the quantile which represents the value 
#less than which a certain percentile of the data lies (50% for median)
def quantile(x, p):
	p_index = int(p * len(x))
	return sorted(x)[p_index]

quantile_10 = quantile(num_friends, 0.1)


#less commenly you want to look at mode, the most common value
def mode(x):
	counts = Counter(x)
	max_count = max(counts.values())
	return [x_i for x_i, count in counts.iteritems()
			if count == max_count]


#dispersion measure how spread out data is. Usually higher values
#indicate more dispersion.

#the simplest measure is range
def data_range(x):
	return max(x) - min(x)


#more complex measure of dispersion is variance 
#first two functions from before
def dot(a, b):
	return sum([a_i * b_i for a_i, b_i in zip(a, b)])

def sum_of_squares(a):
	return dot(a, a)

def de_mean(x):
	x_bar = mean(x)
	return [x_i - x_bar for x_i in x]

def variance(x):
	n = len(x)
	deviations = de_mean(x)
	return sum_of_squares(deviations) / (n - 1)

#when you calculate something on the population it's called a
#parameter (greek). when on a sample it's called a statistic. 

#for population use N and for sample use n

#in the above variance formula n-1 means we're looking at 
#unbiased variance (larger). do this because likely to
#understimate variance. 

#If you plot sample size and sample variance/population variance, 
#you see that low sample sizes significantly underestimate sample variance. 
#when you used biased estimate, we're not approaching population variance. 
#you're aprpoaching (n-1)/n * population variance. you can unbias this by using
#multiplying by n/(n-1). 


#standard deviation is square root of variance. you square and
#root to counter impact of negatives.
def standard_deviation(x):
	return math.sqrt(variance(x))

#like mean, sd also has outlier problem. a robust alternative is
#to comput difference between 75h and 25th percentile values
def interquartile_range(x):
	return quantile(x, 0.75) - quantile(x, 0.25)



#---------------------------------------------
#correlation

#covariance is the paired analogue of variance. whereas variance
#measures how a single variable deviates from its means, covariance
#measures how two variables vary in tandem from their means

#when corresponding elements both above mean or both below means,
#possitive numbers enter sum. else negative numbers. 
def covariance(x, y):
	n = len(x)
	return dot(de_mean(x), de_mean(y)) / (n - 1)


#but this number sucks because input units often don't make sense. 
#it's also hard to say what constitutes large covariance. 

#that's why it's more common to look at correlation, which divides
#out standard deviations of both variables.
def correlation(x, y):
	stdev_x = standard_deviation(x)
	stdev_y = standard_deviation(y)
	if stdev_x > 0 and stdev_y > 0:
		return covariance(x, y) / (stdev_x * stdev_y)
	else:
		return 0

#correlation is unitless and lies between -1 (perfect anticorrelation)
#and 1. 

#sometimes good to remove outliers individually since correlation
#is also strongly affected by outliers. could be a test account data point



#---------------------------------------------
#simpson's paradox

#correlations can be misleading when confounding variables are ignored

#key issue is correlation is measuring the relationship between 2 variables
#all else being equal. this is a poor assumption. 

#the way to avoid this is to know your data. 



#---------------------------------------------
#other correlational caveats

#a correlation of zero indicates there is no linear relationship between 2 variables.
#there could be other relationships though

x = [-2, -1, 0, 1, 2]
y = [2, 1, 0, 1, 2]
#the above have 0 correlation. the relationship is that each element of y equals
#the absolute value of x. what they don't hae is a relationship in which knowing
#how x_i compares to mean(x) gives us info about how y_i compares to mean(y). 

#correlation also says nothing about the size of the relationship.
x = [-2, 1, 0, 1, 2]
y = [99.98, 99.99, 100, 100.01, 10.02]
#these are perfectly correlated bu it's quite possible the relationship
#is not that interesting. 



#---------------------------------------------
#correlation and causation 

#its not the same shit. 
#x could cause y, inverse, both eachother, 3rd factor both, or nada

#can feel more confident about causality by conudcting randomized trials



#---------------------------------------------
#further exploration

#scipy, pandas, and statsmodels have many stats functions
#good stats books are openintro statistics and openstax intro stats


