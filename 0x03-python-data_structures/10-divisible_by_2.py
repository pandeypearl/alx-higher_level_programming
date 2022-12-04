#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    div_two = []

    if len(my_list) == 0:
        return div_two

    div_two = [True if n % 2 == 0 else False for n in my_list]
    return div_two
