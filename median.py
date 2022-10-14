"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        sorted_numbers = sorted(numbers)
        size = len(sorted_numbers)
        if size % 2 == 0:
            half = int(size / 2)
            median = (sorted_numbers[half] + sorted_numbers[half - 1]) / 2
        else:
            half = (size - 1) / 2
            median = sorted_numbers[int(half)]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median)
