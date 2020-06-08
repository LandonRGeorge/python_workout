def pig_latin(word):

    first_letter = word[0]
    remaining_letters = word[1:]

    if first_letter in 'aeiou':
        return word + 'way'

    else:
        return remaining_letters + first_letter + 'ay'
