#!/usr/bin/python3
"""100-my_int

"""


class MyInt(int):
    """
    MyInt that inherits from int
    """
    def __eq__(self, other):
        return int(self) != int(other)

    def __ne__(self, other):
        return int(self) == int(other)
