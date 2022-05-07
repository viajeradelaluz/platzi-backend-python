#!/usr/bin/python3
""" Module of loops with lists and dictionaries in
    comparison with list and dicts comprehensions.
    """


def nested_lists():
    people_i_admire = [
        {'first_name': 'Lynn', 'last_name': 'Margulis'},
        {'first_name': 'Frédéric', 'last_name': 'Copin'},
        {'first_name': 'Maya', 'last_name': 'Angelou'},
    ]

    # Traditional for-loop wit lists
    for item in people_i_admire:
        print(f"{item['first_name']}: {item['last_name']}")

    # List comprehension to traverse lists
    print(f"{[items for items in people_i_admire]}")


def nested_dicts():
    number_classification = {
        'natural_nums': [1, 7, 56, 250],
        'integers_nums': [-2, 10, 12, -5, 9],
        'rational_nums': [-3.4, 5.5, 9.5, ]
    }

    # Traditional for-loop with dicts:
    # Print the value only if its multiplication by 2
    # results in an even number:
    for key, value in number_classification.items():
        value_by_2 = []
        for i in range(len(value)):
            if (value[i] * 2) % 2 == 0:
                value_by_2.append(value[i] * 2)
        print(f"{key}: {value_by_2}")

    # List comprehension inside the dict:
    # Same exercise as above:
    for key, value in number_classification.items():
        value_by_2 = [i*2 for i in value if (i*2) % 2 == 0]
        print(f"{key}: {value_by_2}")


def list_challenge():
    # Create a list of all multiples of 4 that are also multiples
    # of 6 and 9 (36 is their mcm) in a range from 1 to 999,999.
    # Print only the first 15 results.

    spectrum = range(1, 1000000)
    numbers = [i for i in spectrum if i % 36 == 0]
    print(numbers[:15])


def dict_challenge():
    # Create a dictionary where the keys are the numbers from 1 to 100
    # and the values are the result of multiplying the keys by 3. 
    # Store only the odd numbers.

    # Loops way:
    table_of_3 = {}
    for n in range(1, 101):
        if n % 2 != 0:
            table_of_3[n] = n * 3
    print(table_of_3)

    # Dict comprehension way:
    table_of_3 = {n: n*3 for n in range(1, 101) if n % 2 != 0}
    print(table_of_3)

def pow_dict_challenge():
    # Pow dict:
    # Create a dictionary whose keys hold the first 100 natural numbers 
    # with their square roots as values.
    pow_dict = {n: round(n**0.5, 2) for n in range(1, 101)}
    print(pow_dict)


    # Entry point
if __name__ == '__main__':
    option = int(input("""
Select an exercise:
    [1] - Nested lists
    [2] - Nested dicts
    [3] - List challenge
    [4] - Dict challenge
    [5] - Pow dict challenge
> """))
    
    if option == 1:
        nested_lists()
    elif option == 2:
        nested_dicts()
    elif option == 3:
        list_challenge()
    elif option == 4:
        dict_challenge()
    else:
        pow_dict_challenge()
