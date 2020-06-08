def pig_latin_word(word):

    first_letter = word[0]
    remaining_letters = word[1:]

    if first_letter in 'aeiou':
        return word + 'way'

    else:
        return remaining_letters + first_letter + 'ay'


def pig_latin_sentence(sentence):

    sentence_split = sentence.split()
    return ' '.join([pig_latin_word(word) for word in sentence_split])


altered = pig_latin_sentence('this is a test translation')
print(altered)
