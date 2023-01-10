#!/usr/bin/python3
"""1-write_file

"""
def number_of_lines(filename=""):
    """
    Writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, encoding='utf-8') as f:
        return len(f.readlines())
