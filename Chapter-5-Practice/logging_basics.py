#Converts a calculator function to u
import logging


def divide(a, b):
    logging.debug("Dividing numbers")
    return a / b


numbers = [(10, 2), (5, 0), (8, 4)]

for x, y in numbers:
    print(divide(x, y))
