from random import randint

number_random = randint(1, 100)

while True:
    number_chosen = int(input('Enter a number between 1 and 100: '))

    if number_chosen == number_random:
        print('Just right!')
        break

    if number_chosen < number_random:
        print('Too low!')

    if number_chosen > number_random:
        print('Too high!')
