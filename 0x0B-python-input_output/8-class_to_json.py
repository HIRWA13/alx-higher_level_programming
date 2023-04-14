#!/usr/bin/python3

"""
Python Module created by @Jr Hirwa
"""


def class_to_json(obj):
    """
    function that creates a json representation of an object
    Arguments:
        obj (obj): The object entered to create a class
    Return:
        A json representation
    """
    return {key: value for (key, value) in obj.__dict__.items()
            if key in list(obj.__dict__.keys())}
