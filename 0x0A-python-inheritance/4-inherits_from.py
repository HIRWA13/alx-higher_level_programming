#!/usr/bin/python3

"""
Python Module created by @Jr Hirwa
"""


def inherits_from(obj, a_class):
    """
    check wether an object is an instance of a class
    """
    if not isinstance(a_class, type):
        raise TypeError("invalid a_class type")
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
