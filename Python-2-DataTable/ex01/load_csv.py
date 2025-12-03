import pandas as pd


def isFileAccessible(FileName):
    """"Check if a file is accessible for reading."""
    try:
        file = open(FileName, 'r')
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: An error occurred while opening the file.")
    finally:
        try:
            file.close()
        except NameError:
            pass


def load(path: str) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    isFileAccessible(path)
    data = pd.read_csv(path)
    print(type(data))
    return data
