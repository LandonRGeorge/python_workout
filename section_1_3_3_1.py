def my_sum(numbers, starting_point=0):
    """Re-reimplement standard `sum` function"""

    for number in numbers:
        starting_point += number

    return starting_point
