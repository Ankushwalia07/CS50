import random
import sys


def main():
    level = positive_level()
    guess = random.randint(1, level)
    num = positive_guess()
    if num < guess:
        print("Too Small!")
    elif num > guess:
        print("Too Large!")
    else:
        print("Just right!")
        sys.exit()


def positive_level():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            pass
    return n


def positive_guess():
    while True:
        try:
            n = int(input("Guess: "))
            if n > 0:
                break
        except ValueError:
            pass
    return n


main()
