# Guessing Game
import random


def even_odd(guess):
    if guess % 2 == 0:
        print("Also an even number")
    else:
        print('Also an odd number')


print('Enter if you dare ')
print("Beat me at my own game, I'll be fair to you ")
print('I am currently thinking of a number between 1 & 100...')

guess = random.randint(0, 99)
for i in range(5):
    try:
        x = int(input('what number am I thinking about? '))
        if x == guess:
            print("Eureka, Sure u ain't psychic")
            break
        elif x > 100 or x < 0:
            print("I am somewhere in between 1 & 100, let's be guided!")
        else:
            if x < guess:
                print("Better luck next time. Here is a hint: I'm bigger than that, O Ye of little mind")
                even_odd(guess)
            else:
                print("Easy there big fella, I ain't that big. Better luck next time")
                even_odd(guess)
    except ValueError:
        print("Enter the number in digits, not words")
print("I went easy on you, the simple answer is " + str(guess))
