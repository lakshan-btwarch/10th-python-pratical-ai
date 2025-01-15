# Code to count the frequency of elements in a list
elements = list(map(int, input("Enter elements separated by space: ").split()))
frequency = {}

for element in elements:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

print("Frequency of each element:")
for key, value in frequency.items():
    print(f"{key}: {value}")
