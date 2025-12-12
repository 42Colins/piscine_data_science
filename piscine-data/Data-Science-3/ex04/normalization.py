import seaborn as sns
import numpy as np
import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from load_csv import load


def main():
    scaler = MinMaxScaler()
    data = load("../Train_knight.csv")
    datadrop = data.drop('knight', axis=1)

    datastd = scaler.fit_transform(datadrop)
    print("Train knight (scaled) sample:\n", pd.DataFrame(datastd, columns=datadrop.columns).head())

    display = pd.DataFrame(data=datastd, columns=datadrop.columns)
    display['knight'] = data['knight']
    sns.scatterplot(data=display, x='Prescience', y='Empowered', hue="knight", palette=['red','blue'], alpha=0.5)
    plt.show()

    datatest = load("../Test_knight.csv")
    datatest_std = scaler.transform(datatest)
    # print("Test knight (scaled) sample:\n", pd.DataFrame(datatest_std, columns=datatest_std.columns).head())

    display_test = pd.DataFrame(data=datatest_std, columns=datatest.columns)
    sns.scatterplot(data=display_test, x='Prescience', y='Empowered', color='green', alpha=0.5)
    plt.show()


if (__name__ == "__main__"):
    main()