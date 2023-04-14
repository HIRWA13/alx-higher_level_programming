#!/usr/bin/python3

"""
Python Moduke created by @Jr Hirwa
"""
import json


def from_json_string(my_str):
    """
    function to convert a json string to a python object
    Arguments:
        my_obj (str): The entered object to convert in json format
    Return:
        A Python object converted from json
    """
    return json.loads(my_str)
