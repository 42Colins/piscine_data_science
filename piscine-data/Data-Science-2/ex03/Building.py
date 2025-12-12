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


def bargraph(data: pl.DataFrame):
    print(data)
    freq_values = (
    data.select(pl.col("user_id").value_counts())
      .unnest("user_id")
      .select("count")
      .to_series()
      .to_list()
    )
    sns.set_theme(style="darkgrid")
    sns.histplot(data=freq_values, binwidth=10)
    plt.xlabel("Frequency")
    plt.ylabel("Customers")
    plt.xlim(0, 40)
    plt.show()


def bargraphsecond(data: pl.DataFrame):
    sum_prices = data.group_by("user_id").agg(pl.col("price").sum().alias("sumprices"))
    sns.set_theme(style="darkgrid")
    sns.histplot(data=sum_prices, x="sumprices", binwidth=50)
    plt.xlabel("Moneraty value in ₳")
    plt.ylabel("Customers")
    plt.xlim(0, 300)
    plt.show()


def main():
    data = importdatabase()
    bargraph(data)
    bargraphsecond(data)


if (__name__ == "__main__"):
    main()