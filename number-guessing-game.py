# generate a random number
#   loop
# ask the user to make a guess
# if not a valid number
#   print an KeyError
# if number is less than the guess
#   print too low
# if number is greater than guess
#   print too high
# else
#   print well done

import random

number = random.randint(1, 100)

while True:
    guess = input("Please guess the number: ")

    if not guess.isdigit():
        print("Invalid number. Please enter a valid integer.")

    guess = int(guess)

    if guess < number:
        print("Number is too low.")
    elif guess > number:
        print("Number is too high.")
    else:
        print("You have guessed correctly!")
        break
