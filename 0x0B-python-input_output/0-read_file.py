#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python Module created by @Jr Hirwa
"""


def read_file(filename=""):
    """
    function that Reads a file file
    Arguments:
        filename (str): The name of the file to open
    """
    with open(filename, encoding='utf-8') as my_file:
        print(my_file.read(), end='')
