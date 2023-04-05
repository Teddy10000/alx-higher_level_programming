#!/usr/bin/python3
""" creating the student class """


class Student:
    """ Defining the class"""
    def __init__(self, first_name, last_name, age):
        """ Initializing the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves the dictionary representation """
        if (type(attrs)) == list and all(type(i) == str for i in attrs):
            return {f: getattr(self, f) for f in attrs if hasattr(self, f)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """update all the attributtes of student"""
        for item in json:
            self.__dict__.update({item: json[item]})
