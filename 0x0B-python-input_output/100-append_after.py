#!/usr/bin/python3
"""A function that does the insertion"""


def append_after(filename="", search_string="", new_string=""):
    """inserting lines to the function"""
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as doc:
        for line in lines:
            if search_string in line:
                doc.write(line + new_string)
            else:
                doc.write(line)
