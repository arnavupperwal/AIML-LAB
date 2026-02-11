import random
import statistics

marks = [random.randint(0,100) for _ in range(100)]
print("original marks:\n", marks)

mean_marks = statistics.mean(marks)
median_marks = statistics.median(marks)

try:
    mode_marks = statistics.mode(marks)
except statistics.StatisticsError:
    mode_marks = "no unique mode"

print("\nMean: ", mean_marks)
print("Median: ", median_marks)
print("Mode: ", mode_marks)

st_dev = statistics.stdev(marks)
lower_sigma = mean_marks - st_dev
upper_sigma = mean_marks + st_dev

outliers_sigma = [x for x in marks if x < lower_sigma or x > upper_sigma]
print("\noutliers based on mean +- sigma :\n", outliers_sigma)

sorted_marks = sorted(marks)
q1 = statistics.quantiles(sorted_marks, n = 4)[0]
q2 = statistics.median(sorted_marks)
q3 = statistics.quantiles(sorted_marks, n = 4)[2]
iqr = q3 - q1 
lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

outliers_iqr = [x for x in marks if x < lower_limit or x > upper_limit]
print("\nOutliers based on IQR: ", outliers_iqr)

cleaned_marks = [x for x in marks if lower_limit <= x <= upper_limit]
print("\nCleaned marks (Without Outliers):\n", cleaned_marks)
print("\nNumber of marks after removing outliers: ", len(cleaned_marks))
