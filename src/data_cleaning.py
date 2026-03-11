import pandas as pd


def load_data(path):
    
    df = pd.read_excel("data/Online Retail.xlsx")

    return df

def clean_data(df):

    df = df.dropna(subset=["CustomerID"])

    df = df[df["Quantity"] > 0]

    df = df[df["UnitPrice"] > 0]

    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    return df