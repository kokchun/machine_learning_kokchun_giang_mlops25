from constants import DATA_PATH
import pandas as pd 

df = pd.read_csv(DATA_PATH / "Sales.csv")


if __name__ == "__main__":
    print(df)