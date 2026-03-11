import pandas as pd
import datetime as dt


def create_rfm(df):

    snapshot_date = df["InvoiceDate"].max() + dt.timedelta(days=1)

    # tạo bảng RFM
    rfm = df.groupby("CustomerID").agg({
        "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
        "InvoiceNo": "count",
        "TotalPrice": "sum"
    })

    rfm.columns = ["Recency", "Frequency", "Monetary"]

    return rfm