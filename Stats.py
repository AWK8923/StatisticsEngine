def bcalc(n, sumx, sumy, m):
    return (sumy - (m * sumx)) / n


def firstquartile(data):
    if len(data) % 2 != 0:
        h1 = []
        for i in range(round(len(data) / 2) + 1):
            h1.append(i)
        return median(h1)
    else:
        return data[int(len(data) / 4)]


def interquartilerange(data):
    return thirdquartile(data) - firstquartile(data)


def linearregression(x, y):
    n = len(x)
    sumx = sum(x)
    sumy = sum(y)
    sumxy = 0
    sumx2 = 0
    sumy2 = 0

    for i in range(len(x)):
        sumxy += x[i] * y[i]
        sumx2 += pow(x[i], 2)
        sumy2 += pow(y[i], 2)

    m = mcalc(n, sumx, sumy, sumxy, sumx2)
    b = bcalc(n, sumx, sumy, m)
    r = rcalc(n, sumx, sumy, sumxy, sumx2, sumy2)

    print("Equation: %fx + %f\nr= %f\nr^2 = %f" % (m, b, r, pow(r, 2)))


def mcalc(n, sumx, sumy, sumxy, sumx2):
    return ((n * sumxy) - (sumx * sumy)) / ((n * sumx2) - (pow(sumx, 2)))


def mean(data):
    return sum(data) / len(data)


def median(data):
    length = len(data)
    if length % 2 != 0:
        return data[int(round(length / 2))]
    else:
        n1 = data[int((length / 2) - 1)]
        n2 = data[int(length / 2)]
        return n1 + ((n2 - n1) / 2)


def onevariablestatistics(data):
    print("Mean = %.5f\n"
          "Summation = %.5f\n"
          "Summation Squared = %.5f\n"
          "Sum of Squared Differences = %.5f\n"
          "Sample Standard Deviation = %.5f\n"
          "Population Standard Deviation = %.5f\n"
          "Number of Data Points = %.0f\n"
          "Minimum = %.5f\n"
          "First Quartile = %.5f\n"
          "Median = %.5f\n"
          "Third Quartile = %.5f\n"
          "Maximum = %.5f\n"
          "Interquartile Range = %.5f"
          % (mean(data), sum(data), pow(sum(data), 2), sumofsquareddifferences(data), samplestandarddeviation(data),
             populationstandarddeviation(data), len(data), min(data), firstquartile(data), median(data),
             thirdquartile(data), max(data), interquartilerange(data)))


def populationstandarddeviation(data):
    return pow(populationvariance(data), .5)


def populationvariance(data):
    return sumofsquareddifferences(data) / len(data)


def rcalc(n, sumx, sumy, sumxy, sumx2, sumy2):
    return ((n * sumxy) - (sumx * sumy)) / (pow((n * sumx2) - (pow(sumx, 2)), .5) * pow((n * sumy2) - (pow(sumy, 2)), .5))


def samplestandarddeviation(data):
    return pow(samplevariance(data), .5)


def samplevariance(data):
    return sumofsquareddifferences(data) / (len(data) - 1)


def sumofsquareddifferences(data):
    ssd = 0
    m = mean(data)

    for i in data:
        ssd += pow((i - m), 2)

    return ssd


def thirdquartile(data):
    if len(data) % 2 != 0:
        h1 = []
        for i in range(round(len(data) / 2) + 1, len(data)):
            h1.append(i)
        return median(h1)
    else:
        return data[int(len(data) / 4) * 3]
