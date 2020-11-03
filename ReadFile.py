def read(filename):
    data = []

    f = open(filename)
    for i in f:
        data.append(float(i))
    return data


def verifile(x, y):
    if len(x) != len(y):
        print("Dataset lengths mismatch.\n Exiting program...")
        quit()
