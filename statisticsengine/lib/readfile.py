import importlib.resources as pkg_resources
from decimal import Decimal

import statisticsengine.data


def read(filename):
    data = []

    f = pkg_resources.read_text(statisticsengine.data, filename).splitlines()
    for i in f:
        data.append(Decimal(i))

    data.sort()
    return data


def verifile(x, y):
    if len(x) != len(y):
        print("Dataset lengths mismatch.\n Exiting program...")
        quit()
