from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from load_csv import load
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    datatrain = load(sys.argv[1])
    datatest = load(sys.argv[2])

    target = datatrain['knight']
    datatrain = datatrain.drop('knight', axis=1)
    x_split, x_val, y_split, y_val = train_test_split(
    datatrain,
    target,
    test_size=0.2,
    random_state=42)

    tree = DecisionTreeClassifier(random_state=42)
    tree.fit(x_split, y_split)

    predicted_values = tree.predict(x_val)
    f1 = f1_score(y_val, predicted_values, pos_label='Jedi')
    print(f"F1 score on validation: {f1:.2%}")

    tree.fit(datatrain, target)
    predictedtxt = tree.predict(datatest)

    f = open('Tree.txt', 'w')
    for pred in predictedtxt:
        f.write(f"{pred}\n")

    plt.figure(figsize=(16,8))
    plt.title('Decision Tree')
    plot_tree(tree, filled=True, feature_names=datatrain.columns, 
          class_names=['Jedi', 'Sith'], fontsize=6, rounded=True, max_depth=30)
    plt.show()

if (__name__ == "__main__"):
    main()