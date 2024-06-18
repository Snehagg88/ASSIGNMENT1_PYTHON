def min_and_max(numbers):
    return min(numbers), max(numbers)


numbers = [1, 2, 3, 4, 5, -1, 10]
minimum, maximum = min_and_max(numbers)
print("Minimum:", minimum)
print("Maximum:", maximum)
