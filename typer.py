import os
from msvcrt import getch

word = "kacsa"
splitted =


print("[ ] "* len(word))


def get_guess():
    guess = ""
    while guess == "":
        guess = input("What is your guess: ")
    return guess

get_guess()

def validate_guess():
    pass

def guess_correct():
    pass