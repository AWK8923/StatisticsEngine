import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def createplot(x, y, xlabel, ylabel, title):
    xdata = np.array(x)
    ydata = np.array(y)
    frame = pd.DataFrame({xlabel: xdata, ylabel: ydata})

    plt.figure(figsize=(16, 9))
    plt.title(title)

    sns.regplot(x=xlabel,
                y=ylabel,
                data=frame).get_figure().savefig(title)
