import seaborn as sns
import numpy as np
import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler


def main():
    datatrain = pd.read_csv("../Train_knight.csv")

    datatrain = datatrain.drop("knight", axis=1)
    pca = PCA()
    scaler = MinMaxScaler()

    normalized_df_train = scaler.fit_transform(datatrain)

    pca_df_train = pca.fit(normalized_df_train)

    variances = np.array(pca.explained_variance_ratio_ * 100)

    cumulative_variances = []
    cumulative_sum = 0
    for var in variances:
        cumulative_sum += var
        cumulative_variances.append(cumulative_sum)

    var_sum = np.array(cumulative_variances)

    print("Variances (%)")
    print(variances)

    print("Variances cumul")
    print(var_sum)

    plt.figure()
    sns.set_theme(style="darkgrid")
    plt.plot(range(1, len(cumulative_variances) + 1), cumulative_variances)
    plt.xlabel("Number of components")
    plt.ylabel("Explained variances %")
    plt.show()

if (__name__ == "__main__"):
    main()
