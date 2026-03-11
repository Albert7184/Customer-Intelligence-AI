from sklearn.ensemble import RandomForestClassifier

def train_churn_model(rfm):

    # Create churn label
    rfm["Churn"] = (rfm["Recency"] > 180).astype(int)

    X = rfm[["Recency","Frequency","Monetary"]]
    y = rfm["Churn"]

    model = RandomForestClassifier(n_estimators=100)

    model.fit(X,y)

    rfm["Churn_Prediction"] = model.predict(X)

    return rfm, model