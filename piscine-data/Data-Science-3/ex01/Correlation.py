import seaborn as sns
import numpy as np
import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def main():
    data = load("../Train_knight.csv")
    data['knight'] = data['knight'].replace('Jedi', 1)
    data['knight'] = data['knight'].replace('Sith', 0)
    correlation = data.corr().abs()
    print(correlation['knight'].sort_values(ascending=False).to_string())

if (__name__ == "__main__"):
    main()