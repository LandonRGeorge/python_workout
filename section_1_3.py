def my_sum(*numbers):
    """Re-implement standard `sum` function"""

    value = 0
    for number in numbers:
        value += number

    return value
