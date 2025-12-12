import seaborn as sns
import numpy as np
import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load
from sklearn.model_selection import train_test_split


def main():
    data = load("../Train_knight.csv")
    train, validation = train_test_split(
        data,
        test_size=0.2,
        random_state=14,
        stratify=data['knight']
    )

    train.to_csv('Training_knight.csv', index=False)
    validation.to_csv('Validation_knight.csv', index=False)


if (__name__ == "__main__"):
    main()