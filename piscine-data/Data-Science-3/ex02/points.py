import seaborn as sns
import numpy as np
import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def points(datatrain, datatest):
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
    sns.scatterplot(data=datatrain, x='Prescience', y='Empowered', hue='knight', palette=['red','blue'], alpha=0.5, ax=axes[0, 0])
    axes[0, 0].set_title('Knight_train.csv')
    sns.scatterplot(data=datatest, x='Prescience', y='Empowered', color='green', alpha=0.5, ax=axes[0, 1])
    axes[0, 1].set_title('Knight_test.csv')

    sns.scatterplot(data=datatrain, x='Push', y='Deflection', hue='knight', palette=['red','blue'], alpha=0.5, ax=axes[1, 0])
    sns.scatterplot(data=datatest, x='Push', y='Deflection', color='green', alpha=0.5, ax=axes[1, 1])
    plt.show()


def main():
    datatrain = load("../Train_knight.csv")
    datatest = load("../Test_knight.csv")
    points(datatrain, datatest)

if (__name__ == "__main__"):
    main()