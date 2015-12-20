import os
from msvcrt import getch

word = "kacsa"
word_letters = []
process_word = "."* len(word)

for i in word:
    word_letters.append(i)


def get_guess():
    guess = ""
    while guess == "":
        guess = input("What is your guess: ")
    return guess


def validate_guess():
    pass

def guess_correct(guess):
    # process_word_with_correct_letters = ""
    # while process_word_with_correct_letters != word:
        for i in word_letters:
            if i == guess:
                index = word_letters.index(i)
                process_word_with_correct_letters = process_word.replace(process_word[index],i,1)
                print(index)
                # guess_correct(get_guess())

# def take_guesses():
#     process_word_with_correct_letters = ""
#     while process_word_with_correct_letters != word:






guess_correct(get_guess())