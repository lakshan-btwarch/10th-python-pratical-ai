# Code to check if a number is an Armstrong number
number = int(input("Enter a number: "))
temp = number
sum_of_cubes = 0

while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //= 10

if number == sum_of_cubes:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
