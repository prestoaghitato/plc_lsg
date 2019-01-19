import pandas as pd

def calculate_medians(filename):
    df = pd.read_csv(filename)
    df_medians = df.groupby("signals-interval").median()
    df_medians.to_csv("df_medians.csv")


if __name__ == "__main__":
    calculate_medians("dummy.csv")
