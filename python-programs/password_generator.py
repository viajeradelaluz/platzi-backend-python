#!/usr/bin/python3
""" Password generator:

Generates passwords randomly and securely.
    """

import random


def generate_password():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    chars = ['!', '#', '$', '%', '&', '(', ')', '*',
             '+', '-', '/', ':', ';', '<', '=', '>', '?']

    full_chars = mayus + min + nums + chars

    password = []
    for i in range(12):
        random_char = random.choice(full_chars)
        password.append(random_char)
    password = ''.join(password)

    return password


# Entry point
if __name__ == "__main__":
    password = generate_password()
    print(f"""
    +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
··· |P|A|S|S|W|O|R|D| |G|E|N|E|R|A|T|O|R| ···
    +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+

Password: {password}""")
