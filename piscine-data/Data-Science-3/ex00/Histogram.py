import seaborn as sns
import numpy as np
import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def importdatabase() -> pl.DataFrame | None:
    """Import the database using pandas"""
    data = load("../Test_knight.csv")
    ax = data.hist(grid=False, bins=40, alpha=0.5, figsize=(16,8), color="green")
    for a in ax.flatten():
        a.legend(("Knight", "aaa"))
    plt.tight_layout()
    plt.show()
    return data


def plot_knight_histograms():
    """
    Génère des histogrammes superposés pour les colonnes numériques, 
    séparant les données selon que le 'knight' est 'jedi' ou 'sith'.
    """
    data = load("../Train_knight.csv")
    if data is None:
            return

    numeric_columns = data.select_dtypes(include=["float64", "int64"]).columns
    n_cols = len(numeric_columns)

    cols_per_row = 5
    n_rows = (n_cols + cols_per_row - 1) // cols_per_row

    fig, axes = plt.subplots(n_rows, cols_per_row, figsize=(16, 20))

    axes_flat = axes.flatten()

    jedi_data = data[data["knight"] == "Jedi"]
    sith_data = data[data["knight"] == "Sith"]

    for i, column in enumerate(numeric_columns):
        ax = axes_flat[i]

        jedi_values = jedi_data[column].dropna()
        sith_values = sith_data[column].dropna()

        ax.hist(jedi_values, color="blue", bins=40, alpha=0.5, label="Jedi")
        ax.hist(sith_values, color="red", bins=40, alpha=0.5, label="Sith")
        ax.set_title(column, fontsize=8)
        ax.legend(fontsize=8)
        ax.tick_params(axis="both", which="major", labelsize=8)

    plt.tight_layout(pad=5.0)
    plt.show()


def main():
    # importdatabase()
    plot_knight_histograms()

if (__name__ == "__main__"):
    main()