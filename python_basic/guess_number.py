#!/usr/bin/python3
""" Guess the number!

The computer chooses a random number between 0 and 100 and
you have to guess it by following the clues.
    """

import random


def guess_number(n, random_num):
    if n == random_num:
        print(f"\nComputer number: {random_num}\n"
              f"--> You win!")
        return
    if random_num > n:
        n = int(input("Try a larger number: "))
    else:
        n = int(input("Try a smaller number: "))
    guess_number(n, random_num)

# Entry point
if __name__ == "__main__":
    random_num = random.randint(1, 100)
    n = int(input("""
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
···|G|U|E|S|S| |T|H|E| |N|U|M|B|E|R|!|···
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Choose a number between 0 and 100:
> """))

    guess_number(n, random_num)
