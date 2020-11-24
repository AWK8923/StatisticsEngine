import math
from decimal import Decimal

import matplotlib.pyplot as plt
import numpy as np
import pandas
import seaborn

from statisticsengine.lib import readfile


def bcalc(n: Decimal, sumx: Decimal, sumy: Decimal, m: Decimal) -> Decimal:
    # Math: \frac{\sum y-m(\sum x)}{n}
    return Decimal((sumy - (m * sumx)) / n)


def createboxplot(data: list):
    seaborn.boxplot(x=data, width=.25)
    plt.show()


def createlineplot(x: list, y: list, xlabel: str,
                   ylabel: str, title: str) -> None:
    readfile.verifile(x, y)

    for i in range(len(x)):
        x[i] = float(x[i])
        y[i] = float(y[i])

    xdata = np.array(x)
    ydata = np.array(y)
    frame = pandas.DataFrame({xlabel: xdata, ylabel: ydata})

    plt.figure(figsize=(16, 9))
    plt.title(title)

    seaborn.regplot(x=xlabel,
                    y=ylabel,
                    data=frame).get_figure().savefig(title)
    plt.show()


def firstquartile(data: list):
    if len(data) % 2 != 0:
        h1 = []
        for i in range(round(len(data) / 2) + 1):
            h1.append(i)
        return median(h1)
    else:
        return data[int(len(data) / 4)]


def interquartilerange(data: list) -> Decimal:
    return Decimal(thirdquartile(data) - firstquartile(data))


def linearregression(x: list, y: list) -> None:
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

    m = Decimal(mcalc(n, sumx, sumy, sumxy, sumx2))
    b = Decimal(bcalc(n, sumx, sumy, m))
    r = Decimal(rcalcxy(x, y))

    print("\nEquation: %sx + %s\nr= %s\nr^2 = %s" % (m, b, r, r ** 2))


def mcalc(n: Decimal, sumx: Decimal, sumy: Decimal,
          sumxy: Decimal, sumx2: Decimal) -> Decimal:
    # Math: \frac{n(\sum xy)-(\sum x)(\sum y)}{n(\sum x^{2})-(\sum x)^{2}}
    return Decimal(((n * sumxy) - (sumx * sumy)) / ((n * sumx2) - (sumx ** 2)))


def mean(data: list) -> Decimal:
    return Decimal(sum(data) / len(data))


def median(data: list) -> Decimal:
    if len(data) % 2 != 0:
        return Decimal(data[int(round(len(data) / 2))])
    else:
        n1 = data[int((len(data) / 2) - 1)]
        n2 = data[int(len(data) / 2)]
        return Decimal(n1 + ((n2 - n1) / 2))


def onevariablestatistics(data: list) -> None:
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


def populationstandarddeviation(data: list) -> Decimal:
    return Decimal(math.sqrt(populationvariance(data)))


def populationvariance(data: list) -> Decimal:
    return Decimal(sumofsquareddifferences(data) / len(data))


def rcalc(n: Decimal, sumx: Decimal, sumy: Decimal,
          sumxy: Decimal, sumx2: Decimal, sumy2: Decimal) -> Decimal:
    # Math: \frac{n(\sum xy)-(\sum x)(\sum y)}{\sqrt{n(\sum x^{2})-(\sum x)^{2}}*\sqrt{n(\sum y^{2})-(\sum y)^{2}}}
    return Decimal(((n * sumxy) - (sumx * sumy)) / (Decimal((math.sqrt((n * sumx2) - (sumx ** 2))) * (math.sqrt((n * sumy2) - (sumy ** 2))))))


def rcalcxy(x: list, y: list) -> Decimal:
    n = len(x)
    sumx = Decimal(sum(x))
    sumy = Decimal(sum(y))
    sumxy = 0
    sumx2 = 0
    sumy2 = 0

    for i in range(len(x)):
        sumxy += x[i] * y[i]
        sumx2 += pow(x[i], 2)
        sumy2 += pow(y[i], 2)

    return rcalc(n, sumx, sumy, sumxy, sumx2, sumy2)


def reexpress(x: list, y: list, xlabel: str, ylabel: str, title: str) -> None:
    reexpressed = [None] * len(x)
    f = open("Re-expressed-y.txt", "w")
    if len(x) == 19:
        for i in range(len(x)):
            reexpressed[i] = Decimal(math.sqrt(y[i]))

        linearregression(x, reexpressed)
        createlineplot(x, reexpressed, xlabel, "Square Root of " + ylabel, title)
    if len(x) == 50:
        for i in range(len(x)):
            reexpressed[i] = Decimal(round(math.log(y[i], 10), 3))
            f.write(str(reexpressed[i]) + "\n")
        linearregression(x, reexpressed)
        createlineplot(x, reexpressed, xlabel, "Log of " + ylabel, title)


def samplestandarddeviation(data: list) -> Decimal:
    return Decimal(math.sqrt(samplevariance(data)))


def samplevariance(data: list) -> Decimal:
    return Decimal(sumofsquareddifferences(data) / (len(data) - 1))


def sumofsquareddifferences(data: list) -> Decimal:
    ssd = 0
    m = mean(data)

    for i in data:
        ssd += (i - m) ** 2

    return Decimal(ssd)


def thirdquartile(data: list) -> Decimal:
    if len(data) % 2 != 0:
        h1 = []
        for i in range(round(len(data) / 2) + 1, len(data)):
            h1.append(i)
        return median(h1)
    else:
        return Decimal(data[int(len(data) / 4) * 3])
