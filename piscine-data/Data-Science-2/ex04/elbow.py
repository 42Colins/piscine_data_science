import seaborn as sns
import polars as pl
import matplotlib.pyplot as plt
import psycopg2 as ppg
from sklearn.cluster import KMeans
from datetime import datetime


def importdatabase() -> pl.DataFrame | None:
    """Import the database using pandas"""
    uri = "postgresql://cprojean:mysecretpassword@localhost:5432/piscineds"
    query = """SELECT event_type, event_time, price,
     user_id, user_session FROM customers"""
    try:
        data = pl.read_database_uri(query, uri)
        return data
    except (Exception, ppg.DatabaseError) as error:
        print(error)


def elbow(data: pl.DataFrame):
    last_data = datetime(2023, 3, 1)
    last_data = pl.lit(last_data).cast(pl.Date)
    data = data.with_columns(
            pl.col('event_time').cast(pl.Date,
                                      strict=False).alias('event_time'),
            pl.col('price').cast(pl.Float64, strict=False).alias('price')
            )
    one_day = pl.duration(days=1)
    rfm = data.group_by('user_id').agg(
            recency=((last_data - pl.col('event_time').max()) / one_day)
            .cast(pl.Int64)
            .alias('recency'),
            frequency=pl.col("price").count()
            .cast(pl.Int64)
            .alias('frequency'),
            monetary=pl.col("price").sum()
            .cast(pl.Float64)
            .alias('monetary')
    ).sort('user_id')
    print(rfm)
    rfm.columns = ['user_id', 'recency', 'frequency', 'monetary']
    inertias = []

    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(rfm)
        inertias.append(kmeans.inertia_)

    plt.plot(range(1, 11), inertias, marker='o')
    sns.set_theme(style="darkgrid")
    plt.title('Elbow method')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.show()


def main():
    data = importdatabase()
    dataa = pl.DataFrame(data, strict=False)
    elbow(dataa)


if (__name__ == "__main__"):
    main()
