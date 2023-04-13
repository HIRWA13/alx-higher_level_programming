#!/usr/bin/pytthon3

"""
Python Module created by @Jr Hirwa

"""


def write_file(filename="", text=""):
    """
    function to write into a text file and returns number of
    characters written into it and creates it when it does not exitst

    args:
        filename: name of file
        text: content to write into a file
    """
    with open("my_first_file.txt", 'w') as my_file:
        return my_file.write(text)
