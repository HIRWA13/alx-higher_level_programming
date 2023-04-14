#!/usr/bin/python3

"""
Python MOdule created by @Jr Hirwa
"""
import json


def to_json_string(my_obj):
    """
    Returs a json string containing representation of the object
    Arguments:
        my_obj (str): The inputed object to convert in json format
    Return:
        A json formatted  text
    """
    return json.dumps(my_obj)
