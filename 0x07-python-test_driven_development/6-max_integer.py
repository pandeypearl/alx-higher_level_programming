#!/usr/bin/python3
"""6-max_integer

Module to find the max integer in a list

"""


def max_integer(list=[]):
    """max_integer function

    Function to find and return the max integer in a list of integers

    If the list is empty, the function returns None

    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1

    return result
