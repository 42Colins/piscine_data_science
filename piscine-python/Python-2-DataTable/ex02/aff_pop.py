import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from load_csv import load


def convert_population(data) -> pd.DataFrame:
    """Convert population values to numerical format"""
    for col in data.columns[1:]:  # Skip the 'country' column
        data[col] = data[col].apply(lambda x: float(x[:-1]) * 1e3
                                    if isinstance(x, str) and x.endswith('k')
                                    else float(x[:-1]) * 1e6
                                    if isinstance(x, str) and x.endswith('M')
                                    else float(x[:-1]) * 1e9
                                    if isinstance(x, str) and x.endswith('B')
                                    else x)
    return data


def format_population(x, pos):
    """Format population values to a readable format"""
    if x >= 1000000000:
        return f'{x/1e9:.1f}B'
    elif x >= 1000000:
        return f'{x/1e6:.1f}M'
    elif x >= 1000:
        return f'{x/1e3:.1f}K'
    else:
        return f'{x:.0f}'


def plot_population(data):
    """Plot the population of the two countries"""
    print(data)
    data = convert_population(data)
    print(data)

    searched_country = "France"
    second_country = "Samoa"

    country_filter = data['country'] == searched_country
    country_data = data.loc[country_filter]
    country_filter_2 = data['country'] == second_country
    country_data_2 = data.loc[country_filter_2]

    years = data.columns[1:]
    years = pd.to_numeric(years)
    plt.figure(figsize=(12, 6))
    plt.plot(years[1:250], country_data.iloc[0, 1:250])
    plt.plot(years[1:250], country_data_2.iloc[0, 1:250])
    plt.xlabel('Year')
    plt.ylabel('Population')

    ax = plt.gca()

    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_population))

    plt.title(f'Population of {searched_country} and {second_country}')
    plt.legend([searched_country, second_country])
    plt.show()


def main():
    """Main function"""
    data = load("population_total.csv")
    plot_population(data)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
