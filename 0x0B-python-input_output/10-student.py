#!/usr/bin/python3
""" student class """


class Student:
    """ Defining the class"""
    def __init__(self, first_name, last_name, age):
        """ Initializing the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation for student"""
        if (type(attrs)) == list and all(type(i) == str for i in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__
