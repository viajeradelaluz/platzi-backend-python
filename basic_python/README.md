# Basic Python Course

[platzi](https://platzi.com/cursos/python/) | Facundo García Martoni

<br>

Learn how to program from scratch with the fastest growing language on the planet: Python. Discover what an algorithm is and how to build one. Master variables, functions, data structures, conditionals and loops.

- Make data structures
- Create loops
- Learn about programming tools
- Learn basic Python concepts

## Python basics

- Primitive data
- Arithmetic operators
- Logical and comparison operators
- **First program - Money exchange:** `money_exchange.py` Convert your local currency (Colombian, Mexican or Argentine Pesos) to dollars.

```bash
viajeradelaluz@platzi:~/ basic_python$ ./money_exchange.py

    +-+-+-+-+-+ +-+-+-+-+-+-+-+-+
··· |M|o|n|e|y| |E|x|c|h|a|n|g|e| ···
    +-+-+-+-+-+ +-+-+-+-+-+-+-+-+

I want to convert from:
    [1] - Colombian Peso (COP)
    [2] - Mexican Peso (MXN)
    [3] - Argentine Peso (ARS)
>> 1
Colombian Pesos Amount: 58000
--> $14.6 USD
```

## Programming tools

- Modularize code with functions
- Control structures: if/else
- Working with text: character strings
- Working with text: slices
- **Second program - Palindrome:** `palidrome.py` Check if word or sentence is a palidrome.

```bash
viajeradelaluz@platzi:~/ basic_python$ ./palindrome.py
        .      .
._  _.|*._  _|._. _ ._ _  _
[_)(_]||[ )(_][  (_)[ | )(/,
|         . . .

Enter a word or sentence: Yo soy
--> Yo soy is palindrome!
```

## Loops

- Control structures: `while` loop
- Control structures: `for` loop
- Traversing a strings
- Interrupting cycles with `break` and `continue`
- **Third program - Prime nummers:** `prime_number_test.py` Detects whether a number is prime or not and gets the list of the number dividers.

```bash
viajeradelaluz@platzi:~/ basic_python$ ./prime_number_test.py

    +-+-+-+-+--+-+-+-+--+-+
··· |P|R|I|M|  |N|U|M|  |R| (?) ···
    +-+-+-+-+  +-+-+-+  +-+
             x        xx
             x        .x     
             .        ..

Enter a number: 123
[1, 3, 41, 123]
--> 123 is not a prime number.
```

- **Project - Guess the number! [video game]:** `guess_number.py` The computer chooses a random number between 0 and 100 and you have to guess it by following the clues.

```bash
viajeradelaluz@platzi:~/ basic_python$ ./guess_number.py

   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
···|G|U|E|S|S| |T|H|E| |N|U|M|B|E|R|!|···
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Choose a number between 0 and 100:
> 40
Try a smaller number: 20
Try a smaller number: 10
Try a smaller number: 5
Try a larger number: 7
Try a larger number: 8

Computer number: 8
--> You win!
```

## Data structures

- Lists
- Tuples
- Dictionaries
- **Project  - Password generator:** `password_generator.py` Generates passwords randomly and securely.

```bash
viajeradelaluz@platzi:~/ basic_python$ ./password_generator.py

    +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
··· |P|A|S|S|W|O|R|D| |G|E|N|E|R|A|T|O|R| ···
    +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+

Password: PDj8V;m&(7qQ
```
