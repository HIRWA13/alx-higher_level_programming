#!/usr/bin/python3

"""
Python Module created by @Jr Hirwa
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function to save object to a file
    Arguments:
        my_obj (obj): The inputed object to convert in json format
        filename (str): The name of the output file
    Return:
        A file with a text in jason format
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        return my_file.write(json.dumps(my_obj))
