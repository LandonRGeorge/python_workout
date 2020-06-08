def even_odd_nums(seq):
    even_nums = sum(seq[1::2])
    odd_nums = sum(seq[0::2])
    print([odd_nums, even_nums])


even_odd_nums((10,20,30,40,50,60))