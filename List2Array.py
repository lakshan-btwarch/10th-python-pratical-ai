# Code to convert a Python list to a NumPy array
import numpy as np

# Input list
elements = list(map(int, input("Enter elements of the list separated by space: ").split()))

# Convert to NumPy array
array = np.array(elements)

print("Converted NumPy Array:")
print(array)
