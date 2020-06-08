from random import randint

number_random = randint(1, 100)

attempt = 1

while True:

    if attempt <= 3:
        attempt += 1

        number_chosen = int(input('Enter a number between 1 and 100: '))

        if number_chosen == number_random:
            print('Just right!')
            break

        if number_chosen < number_random:
            print('Too low!')

        if number_chosen > number_random:
            print('Too high!')

    else:
        print('\nYou did not guess in 3 or less chances. Loser!')
        break
