import seaborn as sns
import numpy as np
import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load
from sklearn import metrics


def main():
    datatrain = pd.read_csv("../Train_knight.csv")
    datatrain['knight'] = datatrain['knight'].replace('Jedi', 1)
    datatrain['knight'] = datatrain['knight'].replace('Sith', 2)
    correlation = datatrain.corr()

    plt.figure()
    sns.heatmap(correlation)
    plt.show()


if (__name__ == "__main__"):
    main()
