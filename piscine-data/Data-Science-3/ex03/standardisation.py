import seaborn as sns
import numpy as np
import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from load_csv import load


def main():
    scaler = StandardScaler()
    data = load("../Train_knight.csv")
    datadrop = data.drop('knight', axis=1)
    datastd = scaler.fit_transform(datadrop)
    print("Train knight :\n",datastd)
    display = pd.DataFrame(data=datastd, columns=datadrop.columns)
    display['knight'] = data['knight']
    sns.scatterplot(data=display, x='Prescience', y='Empowered',hue="knight", palette=['red','blue'], alpha=0.5)
    plt.show()



    datatest = load("../Test_knight.csv")
    datateststd = scaler.fit_transform(datatest)
    print("Test knight :\n",datatest)
    display = pd.DataFrame(data=datateststd, columns=datadrop.columns)
    sns.scatterplot(data=datatest, x='Prescience', y='Empowered', color="green", alpha=0.5)
    plt.show()


if (__name__ == "__main__"):
    main()