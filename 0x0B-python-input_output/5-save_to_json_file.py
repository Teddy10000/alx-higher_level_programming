#!/usr/bin/python3
"""writing a JSON Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes a JSON Object to a text file"""
    with open(filename, 'w') as doc:
        json_opened = json.dumps(my_obj) 
        return doc.write(json_opened)
