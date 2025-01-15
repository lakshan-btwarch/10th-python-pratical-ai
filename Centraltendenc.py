# Code to calculate mean, median, and mode
import numpy as np
from statistics import mode

# Data
data = [5, 6, 1, 3, 4, 5, 6, 2, 7, 8, 6, 5, 4, 6, 5, 1, 2, 3, 4]

# Calculate statistics
mean_value = np.mean(data)
median_value = np.median(data)
mode_value = mode(data)

# Print results
print(f"Mean: {mean_value:.2f}")
print(f"Median: {median_value:.2f}")
print(f"Mode: {mode_value}")
