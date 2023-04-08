#!/usr/bin/python3
"""Creates a function to print a square."""


def print_square(size):
    """Print a square in form of # character.
    Args:
        size (int): The height or width of the square.
    Raises:
        TypeError: when size is not an integer.
        ValueError: when size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
