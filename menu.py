import os
from msvcrt import getch

hangman ="""
      ==:======II
        :      II
        :      II
      (°.°)    II
       /I\     II
    >/  I \<   II
        I      II
       I I     II
      I   I    II
               II
;;;;;;;;;;;;;;;;;;;;;;;;
"""


def greetings():
    print("=" * 50)
    print("Welcome in the HANGROBOT game!")
    print("=" * 50)
    print(hangman)

def choose_option(counter):
    space = " " * 5
    before = [space for i in range(3)]
    arrow = "--> "
    before[counter-1] = arrow
    print("Main menu")
    print(before[0] + "Play")
    print(before[1] + "Type a word, and play with that")
    print(before[2] + "Exit")
    print()

def first():
    print("It's not ready yet!")

def second():
    print("It's not ready yet")

def third():
    print("Thank you for the game!")
    exit()


menu_points = [first, second, third]

def the_menu():
    counter = 1
    os.system("cls")
    greetings()
    choose_option(counter)
    while True:
        key = ord(getch())
        if key == 72 and counter > 1:
            counter -= 1
            os.system("cls")
            greetings()
            choose_option(counter)
        elif key == 80 and counter < 3:
            counter += 1
            os.system("cls")
            greetings()
            choose_option(counter)
        elif key == 13:
            menu_points[counter-1]()
            exit()


the_menu()


