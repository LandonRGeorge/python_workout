def my_avg(*numbers):

    value = 0
    for number in numbers:
        value += number

    return value / len(numbers)