#!/usr/bin/python3

"""
Python Module created by @Jr Hirwa
"""


def pascal_triangle(n):
    """
    function that creates a pascal triangle
    Attributes:
        n (int): n exponent for triangle
    Return:
        matrix with values for the triangle
    """
    pascal_t = []
    triangle = []

    for i in range(int(n)):
        new = pascal_t[:]
        new.append(1)
        count = len(pascal_t)
        for i in range(1, count):
            new[i] = pascal_t[i - 1] + pascal_t[i]
        pascal_t = new[:]
        triangle.append(pascal_t)
    return
