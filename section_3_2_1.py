def my_sum(*args):
    result = args[0]
    for arg in args[1:]:
        result += arg
    print(result)
