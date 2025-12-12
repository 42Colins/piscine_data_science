import pandas as pd


def isFileAccessible(FileName):
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
    try:
        isFileAccessible(path)
        data = pd.read_csv(path)
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
    return None
