#!/usr/bin/python3
""" Palindrome program:

    Check if word or sentence is a palidrome.
    """


def palindrome(word):
    word = word.replace(" ", "")
    word = word.lower()
    word_reverse = word[::-1]

    if word == word_reverse:
        return True
    else:
        return False


# Entry point
if __name__ == "__main__":
    text = input("""        .      .
._  _.|*._  _|._. _ ._ _  _
[_)(_]||[ )(_][  (_)[ | )(/,
|         . . .

Enter a word or sentence: """)

    if palindrome(text) is True:
        print(f"--> {text.capitalize()} is palindrome!")
    else:
        print(f"--> {text.capitalize()} is not a palindrome.")
