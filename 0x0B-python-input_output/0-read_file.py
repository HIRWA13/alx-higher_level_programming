#!/usr/bin/python3
"""
Python Module created by @Jr Hirwa
"""


def read_file(filename=""):
    """
    function to open and read a file to stdout

    arg:
        filename: name of file
    """
    with open("my_file_0.txt", encoding="utf-8") as my_file:
        print(my_file.read())
