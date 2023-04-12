#!/usr/bin/python3

"""
Python Module created by @Jr Hirwa
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance of class
    """
    if not isinstance(a_class, type):
        raise TypeError("invalid a_class type")
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
