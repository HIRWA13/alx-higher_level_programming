#!/usr/bin/python3

"""
Python Module created by @Jr Hirwa
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        method init for Student class
        Attributes:
            first_name (str): The first name of student
            last_name (str): The last name of student
            age (int): The age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Represents of Student into json
        Return:
            Student class as a json
        """
        return {key: value for (key, value) in self.__dict__.items()
                if key in list(self.__dict__.keys())}
