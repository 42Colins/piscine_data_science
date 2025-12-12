import seaborn as sns
import numpy as np
import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load
from sklearn import metrics


def main():
    truth = open("truth.txt")
    truth = [line.strip() for line in truth.readlines()]
    truth = np.array(truth)
    prediction = open("predictions.txt")
    prediction = [line.strip() for line in prediction.readlines()]
    prediction = np.array(prediction)

    jedi_tp, jedi_tn, jedi_fp, jedi_fn = 0, 0, 0, 0
    sith_tp, sith_tn, sith_fp, sith_fn = 0, 0, 0, 0
    jedi_count, sith_count = 0, 0
    for i in range(len(prediction)):
        pred = prediction[i]
        true = truth[i]
        if (true == "Jedi"):
            jedi_count += 1
        elif (true == "Sith"):
            sith_count += 1
        if pred == 'Jedi' and true == 'Jedi':
            jedi_tp += 1
            sith_tn += 1
        if pred == 'Jedi' and true == 'Sith':
            jedi_fp += 1
            sith_fn += 1
        if pred == 'Sith' and true == 'Jedi':
            jedi_fn += 1
            sith_fp += 1
        if pred == 'Sith' and true == 'Sith':
            jedi_tn += 1
            sith_tp += 1

    jedi_prec = jedi_tp / (jedi_tp + jedi_fp)
    sith_prec = sith_tp / (sith_tp + sith_fp)
    jedi_recall = jedi_tp / (jedi_tp + jedi_fn)
    sith_recall = sith_tp / (sith_tp + sith_fn)

    jedi_f1 = 2 * jedi_tp / (2 * jedi_tp + jedi_fp + jedi_fn)
    sith_f1 = 2 * sith_tp / (2 * sith_tp + sith_fp + sith_fn)

    print("            precision    recall  f1-score    total ")
    print(f"Jedi :      {jedi_prec:.2f}         {jedi_recall:.2f}       {jedi_f1:.2f}      {jedi_count}")
    print(f"Sith :      {sith_prec:.2f}         {sith_recall:.2f}       {sith_f1:.2f}      {sith_count}")
    print(f"Accuracy :                          {(sith_f1 + jedi_f1) / 2:.2f}      {jedi_count + sith_count}")
    arr = np.array([[jedi_tp, jedi_fn], [jedi_fp, jedi_tn]])
    print(arr)
    matrix = metrics.ConfusionMatrixDisplay(confusion_matrix=arr)
    matrix.plot()
    plt.show()


if (__name__ == "__main__"):
    main()
