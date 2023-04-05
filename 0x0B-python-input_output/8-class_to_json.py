#!/usr/bin/python3
"""A function that returns the dictionary data structure"""


def class_to_json(obj):
    """returning dictionary"""
    return obj.__dict__
