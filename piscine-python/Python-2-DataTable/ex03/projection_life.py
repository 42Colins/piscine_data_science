import matplotlib.pyplot as plt
from load_csv import load


def life_projection_plot(data_expectancy, data):
    """Plot the life expectancy projection"""
    plt.figure(figsize=(12, 6))
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life expectancy')
    plt.scatter(data['1900'], data_expectancy['1900'])
    ax = plt.gca()
    ax.set_xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.title('Year 1900')
    plt.show()


def main():
    """Main function"""
    data_expectancy = load("life_expectancy_years.csv")
    data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_projection_plot(data_expectancy, data)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
