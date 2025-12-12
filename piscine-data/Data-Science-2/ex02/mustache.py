import seaborn as sns
import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2 as ppg


def importdatabase() -> pl.DataFrame | None:
    """Import the database using pandas"""
    uri = "postgresql://cprojean:mysecretpassword@localhost:5432/piscineds"
    query = "SELECT event_type, event_time, price, user_id, user_session FROM customers WHERE event_type = 'purchase'"
    try:
        data = pl.read_database_uri(query, uri)
        return data
    except (Exception, ppg.DatabaseError) as error:
        print(error)


def printRequirements(data: pl.DataFrame) -> pl.DataFrame | None:
    pricedata = data.with_columns(pl.col("price"))
    print("count : ", pricedata['price'].count())
    print("mean  : ", pricedata['price'].mean())
    print("std   : ", pricedata['price'].std())
    print("min   : ", pricedata['price'].min())
    print("25%   : ", pricedata['price'].quantile(0.25))
    print("50%   : ", pricedata['price'].quantile(0.5))
    print("75%   : ", pricedata['price'].quantile(0.75))
    print("max   : ", pricedata['price'].max())
    return


def mustache(data: pl.DataFrame):
    sns.set_theme(style="darkgrid")
    sns.boxplot(x="price", data=data, flierprops={"marker": "d"}, medianprops={"color": "g", "linewidth": 2})
    plt.show()


def mustacheCentered(data: pl.DataFrame):
    sns.set_theme(style="darkgrid")
    sns.boxplot(x="price", data=data, vert=False, showfliers=False)
    plt.show()


def lastmustache(data: pl.DataFrame):
    aggregated_data = data.group_by(['user_id', 'user_session']).agg(
        pl.col("price").sum().alias("basket")
    )
    sns.boxplot(x="basket", data=aggregated_data, flierprops={"marker": "d"}, medianprops={"color": "g", "linewidth": 2})
    plt.xlim(-15,110)
    plt.show()

def main():
    data = importdatabase()
    printRequirements(data)
    # mustache(data)
    # mustacheCentered(data)
    lastmustache(data)

if (__name__ == "__main__"):
    main()