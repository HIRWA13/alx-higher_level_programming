#!/usr/bin/python3
"""Create an addition  integer function."""


def add_integer(a, b=98):
    """Return the addition of a and b.
    Floating arguments are typecased to integers before addition is performed.
    Raises:
        TypeError: If a or b are non-integers and non-floats.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
