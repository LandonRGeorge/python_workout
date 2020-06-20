def sort_by_abs_value(number):
    return abs(number)


numbers = [1, -1, 5, -5, -6, 100, -50]
print(sorted(numbers, key=sort_by_abs_value))