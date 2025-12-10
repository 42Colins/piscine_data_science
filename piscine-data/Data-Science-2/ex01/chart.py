import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import matplotlib.dates as mdate
import seaborn as sns
import psycopg2 as ppg
import polars as pl


def importdatabase() -> pl.DataFrame | None:
    """Import the database using pandas"""
    uri = "postgresql://cprojean:mysecretpassword@localhost:5432/piscineds"
    query = "SELECT event_type, event_time, price, user_id FROM customers WHERE event_type = 'purchase'"
    try:
        data = pl.read_database_uri(query, uri)
        return data
    except (Exception, ppg.DatabaseError) as error:
        print(error)


def lineChart(data):
    try:
        aggregated_data = data.with_columns(pl.col(
            "event_time").dt.truncate("1d"))
        aggregated_data = aggregated_data.group_by('event_time').agg(
            pl.col("event_type").len().alias("daily_sales")
        ).sort("event_time")
        sns.set_theme(style="darkgrid")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.xaxis.set_major_formatter(mdate.DateFormatter("%b"))
        sns.lineplot(data=aggregated_data, x='event_time', y='daily_sales')
        ax.set_xlabel("")
        ax.set_ylabel("")
        plt.show()
    except (Exception) as error:
        print("Error : ", error)


def barChart(data):
    try:
        aggregated_data = data.with_columns(pl.col(
            "event_time").dt.truncate("1mo"))
        aggregated_data = aggregated_data.group_by('event_time').agg(
            pl.col("price").sum().alias("monthly_price")
        ).sort("event_time")
        aggregated_data = aggregated_data.with_columns(
            pl.col("event_time").dt.strftime("%b").alias("event_time_str")
        )
        sns.set_theme(style="darkgrid")
        fig, ax = plt.subplots(figsize=(10, 6))
        month_order = ['Oct', 'Nov', 'Dec', 'Jan', 'Feb']
        sns.barplot(data=aggregated_data, x='event_time_str',
                    y='monthly_price', order=month_order, dodge=False)
        ax.set_xlabel("Month")
        ax.set_ylabel("Total in million of ₳")
        ax.yaxis.set_major_formatter(
            plt.FuncFormatter(lambda x, p: f'{x/1e6:.1f}'))
        plt.show()
    except (Exception) as error:
        print("Error : ", error)


def secondLineChart(data):
    try:
        aggregated_data = data.with_columns(pl.col(
            "event_time").dt.truncate("1d"))
        aggregated_data = aggregated_data.group_by('event_time').agg(
            pl.col("price").mean().alias("average")
        ).sort("event_time")
        aggregated_data = aggregated_data.with_columns(
            pl.col("event_time").dt.strftime("%b").alias("event_time_str")
        )

        sns.set_theme(style="darkgrid")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=aggregated_data, x='event_time', y='average')
        axes.Axes.fill_between(data=aggregated_data, x='event_time',
                               y1='average', ax=ax, alpha=0.3, color='#2E86AB')
        first_date = aggregated_data['event_time'][0]
        year = first_date.year
        start_date = pd.Timestamp(year=year, month=10, day=1)
        end_date = pd.Timestamp(year=year+1, month=2, day=28)
        ax.set_xlim(start_date, end_date)
        ax.set_ylim(0)
        ax.set_xlabel("")
        ax.set_ylabel("Average spend/customers in ₳")
        month_order = ['Oct', 'Nov', 'Dec', 'Jan', 'Feb']
        tick_positions = [
            pd.Timestamp(year=year, month=10, day=15),
            pd.Timestamp(year=year, month=11, day=15),
            pd.Timestamp(year=year, month=12, day=15),
            pd.Timestamp(year=year+1, month=1, day=15),
            pd.Timestamp(year=year+1, month=2, day=15)
        ]
        ax.set_xticks(tick_positions)
        ax.set_xticklabels(month_order)
        plt.show()
    except (Exception) as error:
        print("Error : ", error)


def main():
    """Main function
    Import database then display the pie chart"""
    data = importdatabase()
    lineChart(data)
    barChart(data)
    secondLineChart(data)


if (__name__ == "__main__"):
    main()
