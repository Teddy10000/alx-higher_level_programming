#!/usr/bin/python3
""" creating a class """


class Student:
    """ Defining a student class"""
    def __init__(self, first_name, last_name, age):
        """ Initializing the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ converting to dictionary"""
        return self.__dict__
