#!/usr/bin/python3
""" Takes URL and email, sends POST request to passed URL
with email as parameter, displays body of response"""
import requests
from sys import argv


if __name__ == '__main__':
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
