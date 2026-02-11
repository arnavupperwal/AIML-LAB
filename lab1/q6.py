import statistics 

data = [10,20,30,25,20,40,50]
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
variation = statistics.variance(data)
st_deviation = statistics.stdev(data)

print("the mean of the given data is:", mean)
print("the median of the given data is: ", median)
print("the mode for the given data is: ", mode)
print("the variation of the given data is: ", variation)
print("the standard deviation of the given data is: ", st_deviation)
