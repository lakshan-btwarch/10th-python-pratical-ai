# Code to calculate variance and standard deviation
import statistics

# Data
data = [33, 44, 55, 67, 54, 22, 33, 44, 56, 78, 21, 31, 43, 90, 21, 33, 44, 55, 87]

# Calculate variance and standard deviation
variance = statistics.variance(data)
std_deviation = statistics.stdev(data)

print(f"Variance: {variance:.2f}")