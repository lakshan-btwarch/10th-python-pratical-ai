# Code to generate a number pattern
lines = int(input("Enter the number of lines for the pattern: "))
current_number = 1

for i in range(1, lines + 1):
    for j in range(1, i + 1):
        print(current_number, end=" ")
        current_number += 1
    print()  # Move to the next line
s