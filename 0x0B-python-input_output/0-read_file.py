#!/usr/bin/python3
"""This Fucntion opens and read the context of a file"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as doc:
        print(doc.read(), end="")
