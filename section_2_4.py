def ubbi_dubbi(word):

    letter_list = []
    for letter in word:
        if letter in 'aeiou':
            letter_list.append('ub' + letter)
        else:
            letter_list.append(letter)

    print(''.join(letter_list))