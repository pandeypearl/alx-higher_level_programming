#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    x = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                x += a ** b / i
        except Exception:
            x = b + a
            break

    return x
