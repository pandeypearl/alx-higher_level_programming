#!/usr/bin/python3
"""4-inherits-from

"""


def inherits_from(obj, a_class):
    """
    Returns true if object is instance of a class
    that inherited froma specified class

    Otherwise, returns false
    """
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False
