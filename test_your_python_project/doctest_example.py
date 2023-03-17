def to_absolute(n: int):
    """
    Return the absolute value of the number n.

    :param n: The number to convert
    :return: The absolute value of n

    >>> to_absolute(2)
    2

    >>> to_absolute(-8)
    8
    """
    if n <= 0:
        return -n
    return n


# python -m doctest -v doctest_example.py
