#!/usr/bin/env python3
# Created by: Daniel Momoh
# Created on: Oct 19, 2022.
# This program asks the user to guess a
# number and if they get it wrong they are told so.
import random


def main():
    # Declaration of variables
    number = random.randint(1, 10)
    number_of_guesses = 0
    # Get the guess form the user
    print("okay! I am Guessing a number between 1 and 10:")
    # check to see if guess is right or wrong
    while number_of_guesses < 5:
        guess = int(input())
        number_of_guesses += 1
    if guess < number:
        print("YOU GOT IT RIGHT!")
    else:
        print("Your guess is incorrect")
        print("The number was is {} ".format(number_of_guesses))
    if guess == number:
        print("You guessed the number")


if __name__ == "__main__":
    main()
