import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler

def main():
    try:
        datatrain = pd.read_csv('../Train_knight.csv')
    except Exception:
        print("Error: .csv is not found or bad csv")
        exit()

    data = datatrain.drop('knight', axis=1)

    scaler = StandardScaler()
    data_std = scaler.fit_transform(data)

    transformed = pd.DataFrame(data_std, columns=data.columns)

    vif_data = pd.DataFrame()
    vif_data["Feature"] = transformed.columns
    vif_data["VIF"] = [variance_inflation_factor(transformed.values, i) for i in range(transformed.shape[1])]
    vif_data["Tolerance"] = 1 / vif_data["VIF"]

    print(vif_data.to_string(index=False))
    final = vif_data[vif_data["VIF"] < 5]
    
    print("\n")
    
    final = final.sort_values("VIF", ascending=False)
    print(final.to_string(index=False))


if (__name__ == "__main__"):
    main()