from decimal import *


def read(filename):
    data = []

    f = open(filename)
    for i in f:
        data.append(Decimal(i))

    data.sort()
    return data


def verifile(x, y):
    if len(x) != len(y):
        print("Dataset lengths mismatch.\n Exiting program...")
        quit()
