# Code to swap elements with the next divisible by 5
numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))

for i in range(1, len(numbers)):
    if numbers[i] % 5 == 0:
        numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]

print("List after swapping:", numbers)
