#!/usr/bin/python3

"""
Python text created by @Jr Hirwa
"""


def append_write(filename="", text=""):
    """
    Appends written text a utf-8 encoded text file
    Arguments:
        filename (str): The name of the file to open
        text (str): The text to append
    Return:
        A file with appended text
    """
    with open(filename, 'a', encoding='utf-8') as my_file:
        return my_file.write(text)
