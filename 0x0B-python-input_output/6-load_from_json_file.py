#!/usr/bin/python3
"""6-load_from_json_file

"""
from json import loads


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”
    """
    with open(filename, encoding='utf-8') as f:
        return loads(f.read())
