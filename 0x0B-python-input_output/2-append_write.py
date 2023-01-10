#!/usr/bin/python3
"""2-append_write

"""


def read_lines(filename="", nb_lines=0):
    """
    Appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    """
    with open(filename, encoding='utf-8') as f:
        text = f.readlines()
        tot_lines = len(text)

        if nb_lines <= 0 or nb_lines >= tot_lines:
            f.seek(0)
            print(f.read(), end='')
        else:
            for i in range(nb_lines):
                print(text[i], end='')
