#!/usr/bin/python3

"""
Python Module created by @Jr Hirwa
"""
import json


def load_from_json_file(filename):
    """
    function that loads an object from json file
    Arguments:
        filename (str): The name of the file
    Return:
        A file with a text in json format
    """
    with open(filename, encoding='utf-8') as my_file:
        return (json.loads(my_file.read()))
