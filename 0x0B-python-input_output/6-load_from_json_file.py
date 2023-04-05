#!/usr/bin/python3
"""A Function that creates an Object from a  file”"""
import json


def load_from_json_file(filename):
    """reads the file and then appends an Object from a file”"""
    with open(filename, 'r') as doc:
        return json.load(doc)
