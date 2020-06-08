def describe_strings(*strings):

    min_num = min([len(string) for string in strings])
    max_num = max([len(string) for string in strings])
    avg_num = sum([len(string) for string in strings]) / len(strings)

    return min_num, max_num, avg_num