#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number < 0:
    last = abs(number) % 10
    last = -last
else:
    last = number % 10

print(f"Last digit of {number:d}", end=' ')
print(f"is {last:d} and is", end=' ')

if last > 5:
    print("greater than 5")
elif last == 0:
    print("0")
else:
    print("less than 6 and not 0")
