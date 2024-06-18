def count_occurrences(lst, element):
    return lst.count(element)


numbers = [1, 2, 3, 4, 2, 2, 5, 2]
element = 2
count = count_occurrences(numbers, element)
print(count)
