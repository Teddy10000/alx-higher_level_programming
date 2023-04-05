#!/usr/bin/python3
"""Appends a string of a text file"""


def append_write(filename="", text=""):
    """Appending a string to a text file"""
    with open(filename, 'a') as doc:
        return doc.write(text)
