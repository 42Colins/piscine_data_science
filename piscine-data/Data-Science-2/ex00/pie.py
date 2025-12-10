import pandas as pd
import matplotlib.pyplot as plt
import psycopg2 as ppg


def importdatabase():
    """Import the database using pandas"""
    try:
        co = ppg.connect(dbname="piscineds", user="cprojean", host="localhost",
                         password="mysecretpassword", port=5432)
    except (Exception, ppg.DatabaseError) as error:
        print(error)
    cursor = co.cursor()
    try:
        cursor.execute("SELECT event_type FROM customers")
    except (Exception, ppg.DatabaseError) as error:
        cursor.close()
        print("Error: %s" % error)
    tuples_list = cursor.fetchall()
    cursor.close()
    column_names = ['event_type']
    try:
        df = pd.DataFrame(tuples_list, columns=column_names)
        return df
    except Exception as error:
        print(error)
        return


def pieChart(data):
    try:
        event_counts = data['event_type'].value_counts()
        plt.pie(event_counts.values, labels=event_counts.index,
                autopct='%1.1f%%')
        plt.show()
    except (Exception) as error:
        print("Error : ", error)


def main():
    """Main function
    Import database then display the pie chart"""
    data = importdatabase()
    pieChart(data)


if (__name__ == "__main__"):
    main()
