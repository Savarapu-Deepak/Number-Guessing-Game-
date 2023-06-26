# Number Guessing Game.
import random

lower_Bound = int(input('Enter Lower Bound Value : '))
upper_Bound = int(input('Enter Upper Bound Value : '))

number = random.randint(lower_Bound, upper_Bound)
print('      You Have Only 7 Guessing Chances.')


check = 1
while check <= 7:
    guess = int(input('Guess Any Number With in 1 - 100 : '))
    if guess > number:
        print('Your Guess is High......')
    elif guess == number:
        print('Congrats.....You did it in {} turn'.format(check))
        break
    else:
        print('Your Guess is Low')
    check += 1


