#!/usr/bin/python3

"""
Python Module created by @Jr Hirwa
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    return (type(obj) is a_class)
