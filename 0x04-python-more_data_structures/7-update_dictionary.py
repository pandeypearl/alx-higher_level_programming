#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    n_dictionary = {key: value}
    a_dictionary.update(n_dictionary)
    return a_dictionary
