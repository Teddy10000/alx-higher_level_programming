#!/usr/bin/python3
"""This Fucntion opens and read the context of a file"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as doc:
        print(doc.read(), end="")
