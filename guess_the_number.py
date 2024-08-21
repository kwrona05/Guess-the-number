import random

def guess_the_number():
    number_to_guess = random.randint(1,10)
    your_number = None

    print('Guess the number from 1 to 10')

    while your_number != number_to_guess:
        your_number = int(input('Your number: '))

        if your_number < number_to_guess:
            print('Too low')
        elif your_number > number_to_guess:
            print('Too high')
        else:
            print('Congrats!')

guess_the_number()