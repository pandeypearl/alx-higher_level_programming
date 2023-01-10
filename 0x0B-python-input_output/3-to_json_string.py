#!/usr/bin/python3
"""3-to-json-string

"""
from json import dumps


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    """
    return dumps(my_obj)
