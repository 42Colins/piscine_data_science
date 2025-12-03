import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
from load_csv import load


def main():
    """Main function"""
    data = load("life_expectancy_years.csv")
    searched_country = "France"
    country_filter = data['country'] == searched_country
    country_data = data.loc[country_filter]
    country_data = pd.melt(country_data, id_vars=["country"], var_name="year",
                           value_name="Life expectancy")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=country_data, x="year", y="Life expectancy")
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy (Years)')
    ax = plt.gca()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
