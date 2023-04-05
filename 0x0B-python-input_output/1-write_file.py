#!/usr/bin/python3
"""This is a function that writes to a files."""


def write_file(filename="", text=""):
    """Writing to the file"""
    with open(filename, "w", encoding="utf-8") as doc:
        return doc.write(text)
