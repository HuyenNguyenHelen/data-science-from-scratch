#-------------------------------------------------------------------------
#matplotlib

#primary purpose is to explore data and to communicate data


#-------------------------------------------------------------------------
#matplotlib

#widely used but showing its age
#not great for elaborate interactive web visualizations
#good for simple stuff
#will use matplotlib.pyplot module
#can save with savefig() and display with show()


import matplotlib.pyplot as plt
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300, 330, 700, 950, 1500, 4000, 11000]
#plt.plot(years, gdp, color = 'green', marker = 'o', linestyle = 'solid')
#plt.title('Nominal GDP')
#plt.ylabel("Billion of $")
#plt.show()


#-------------------------------------------------------------------------
#bar charts

#great for showing how some quantity varies among discrete set of items

movies = ["Back to the future", "Iron man", "Fight club", "Avengers"]
num_oscars = [5, 8, 2, 9]

xs = [i + 0.1 for i, _ in enumerate(movies)]
#plt.bar(xs, num_oscars)

#plt.ylabel("Number of Oscars")
#plt.title("My favorite movies")

#plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

#plt.show()

#histogram also good for histograms of bucketed numeric values,
#to see how values are distributed
grades = [83, 84, 91, 75, 66, 51, 99, 81, 77, 74, 71, 72]
decile = lambda grade: grade // 10 * 10

from collections import Counter
histogram = Counter(decile(grade) for grade in grades)

#plt.bar([x + 0 for x in histogram.keys()], histogram.values(), 8)

#plt.axis([-5, 105, 0, 5])
#plt.xticks([1 * i for i in range(11)])
#plt.xlabel("Decile")
#plt.ylabel("# of Students")
#plt.title("Distribution of Exam 1 Grades")
#plt.show()

#for bar charts especially make sure y-axis starts at 0



#-------------------------------------------------------------------------
#line charts

#made with plt.plot()
#great choice for showing trends
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]

#diff from adding because adds element by element
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

#plt.plot(xs, variance, 'g-', label = 'variance')
#plt.plot(xs, bias_squared, 'r-.', label = 'bias^2')
#plt.plot(xs, total_error, 'b:', label = 'total error')

#plt.legend(loc = 9) #automatic because assigned labels
#plt.xlabel("model complexity")
#plt.title("The Bias-Variance Tradeoff")
#plt.show()


#-------------------------------------------------------------------------
#scatterplots

#used to visualize the relationship between two paired sets of data

friends = [78, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

for label, friend_count, minute_count in zip(labels, friends, minutes):
	plt.annotate(label,
		xy = (friend_count, minute_count),
		xytext = (5, -5),
		textcoords = 'offset points')

#plt.title("Daily Minutes vs. Number of Friends")
#plt.xlabel("# of friends")
#plt.ylabel("daily minutes spent on the site")
#if you're scattering comparable variables do plt.axis("equal")
#plt.show()


#-------------------------------------------------------------------------
#further exploration

#seaborn is built on top of matplotlib and is better
#d3.js is a js library for interactive visualizations
#bokeh brings d3-style visualizations to python
#ggoplot is r's port of ggplot2


