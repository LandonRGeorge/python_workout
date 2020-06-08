def firstlast(sequence):
    """Take a sequence and return its first and last elements"""

    output =  sequence[:1] + sequence[-1:]
    print(output)


firstlast([1,2,3,4])