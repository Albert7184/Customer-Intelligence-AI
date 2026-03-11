import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Customer Intelligence Platform",
    layout="wide"
)

# =========================
# LOAD CSS
# =========================

def load_css():
    with open("dashboard/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# =========================
# HEADER
# =========================

st.title("AI Customer Intelligence Platform")

st.markdown("""
<div style="
background:linear-gradient(90deg,#0ea5e9,#6366f1);
padding:20px;
border-radius:15px;
text-align:center;
color:white;
font-size:20px;">
Customer Segmentation • AutoML • AI Insights • Churn Detection • Global Analytics
</div>
""", unsafe_allow_html=True)

# =========================
# DATA UPLOAD
# =========================

st.subheader("Upload Customer Dataset")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel dataset",
    type=["csv", "xlsx"]
)

# =========================
# LOAD DEFAULT DATA
# =========================

@st.cache_data
def load_default_dataset():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR, "data", "Online Retail.xlsx")

    df = pd.read_excel(DATA_PATH)

    return df

# =========================
# LOAD DATA
# =========================

if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    else:
        df = pd.read_excel(uploaded_file)

    st.success("Dataset uploaded successfully")

else:

    df = load_default_dataset()

    st.info("Using default dataset")

# =========================
# DATA VALIDATION
# =========================

required_columns = [
    "CustomerID",
    "InvoiceDate",
    "Quantity",
    "UnitPrice",
    "Country"
]

missing_cols = [col for col in required_columns if col not in df.columns]

if missing_cols:

    st.error(f"Dataset missing columns: {missing_cols}")
    st.stop()

# =========================
# DATA CLEANING
# =========================

df = df.dropna(subset=["CustomerID"])

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# =========================
# RFM FEATURE ENGINEERING
# =========================

snapshot_date = df["InvoiceDate"].max()

rfm = df.groupby("CustomerID").agg({

    "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
    "InvoiceNo": "count",
    "TotalPrice": "sum"

})

rfm.columns = ["Recency", "Frequency", "Monetary"]

rfm = rfm.reset_index()

# =========================
# AUTO CLUSTER OPTIMIZATION
# =========================

def find_best_k(data):

    scores = []

    for k in range(2, 8):

        model = KMeans(n_clusters=k, random_state=42)

        labels = model.fit_predict(data)

        score = silhouette_score(data, labels)

        scores.append((k, score))

    best_k = max(scores, key=lambda x: x[1])[0]

    return best_k


best_k = find_best_k(rfm[["Recency", "Frequency", "Monetary"]])

kmeans = KMeans(n_clusters=best_k, random_state=42)

rfm["Cluster"] = kmeans.fit_predict(
    rfm[["Recency", "Frequency", "Monetary"]]
)

# =========================
# CLUSTER INTERPRETATION
# =========================

cluster_summary = rfm.groupby("Cluster").agg({

    "Recency": "mean",
    "Frequency": "mean",
    "Monetary": "mean",
    "CustomerID": "count"

}).reset_index()

cluster_summary.columns = [
    "Cluster",
    "Avg Recency",
    "Avg Frequency",
    "Avg Monetary",
    "Customers"
]

def label_cluster(row):

    if row["Avg Monetary"] > cluster_summary["Avg Monetary"].mean():
        return "VIP Customers"

    elif row["Avg Frequency"] > cluster_summary["Avg Frequency"].mean():
        return "Loyal Customers"

    elif row["Avg Recency"] > cluster_summary["Avg Recency"].mean():
        return "At Risk Customers"

    else:
        return "Normal Customers"

cluster_summary["Segment"] = cluster_summary.apply(label_cluster, axis=1)

# =========================
# SIMPLE CHURN LABEL
# =========================

rfm["Churn"] = rfm["Recency"].apply(lambda x: 1 if x > 90 else 0)

# =========================
# AUTO ML MODEL COMPARISON
# =========================

X = rfm[["Recency", "Frequency", "Monetary"]]
y = rfm["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

models = {

    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier()

}

results = {}

for name, model in models.items():

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    acc = accuracy_score(y_test, pred)

    results[name] = acc

# =========================
# SIDEBAR CLUSTER FILTER (IMPROVED)
# =========================

cluster_labels = dict(
    zip(cluster_summary["Cluster"], cluster_summary["Segment"])
)

cluster_options = [
    f"{c} - {cluster_labels[c]}" for c in cluster_labels
]

cluster_filter = st.sidebar.multiselect(
    "Select Customer Segments",
    cluster_options,
    default=cluster_options
)

selected_clusters = [
    int(c.split(" - ")[0]) for c in cluster_filter
]

rfm_filtered = rfm[rfm["Cluster"].isin(selected_clusters)]

if len(selected_clusters) == 0:
    st.warning("Please select at least one customer segment.")
    st.stop()

# =========================
# KPI METRICS
# =========================

st.subheader("Business Metrics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Customers", len(rfm_filtered))
c2.metric("Clusters", rfm["Cluster"].nunique())
c3.metric("Best Cluster K", best_k)
c4.metric("Churn Rate", round(rfm_filtered["Churn"].mean(), 2))

# =========================
# TABS
# =========================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Segmentation",
    "Auto ML",
    "Global Map",
    "AI Insights",
    "Dataset"
])

# =========================
# SEGMENTATION
# =========================

with tab1:

    st.subheader("Customer Segmentation")

    fig = px.scatter(
        rfm_filtered,
        x="Recency",
        y="Monetary",
        size="Frequency",
        color="Cluster",
        hover_data=["CustomerID"]
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Cluster Explanation")

    filtered_summary = cluster_summary[
        cluster_summary["Cluster"].isin(selected_clusters)
    ]

    st.dataframe(filtered_summary)

# =========================
# AUTOML
# =========================

with tab2:

    st.subheader("Auto ML Model Comparison")

    model_df = pd.DataFrame({
        "Model": results.keys(),
        "Accuracy": results.values()
    })

    fig = px.bar(
        model_df,
        x="Model",
        y="Accuracy",
        color="Model"
    )

    st.plotly_chart(fig, use_container_width=True)

    best_model = max(results, key=results.get)

    st.success(f"Best Model: {best_model}")

# =========================
# GLOBAL MAP
# =========================

with tab3:

    st.subheader("Customer World Distribution")

    country_counts = df["Country"].value_counts().reset_index()

    country_counts.columns = ["Country", "Customers"]

    fig = px.choropleth(
        country_counts,
        locations="Country",
        locationmode="country names",
        color="Customers"
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================
# AI INSIGHTS
# =========================

with tab4:

    st.subheader("AI Business Insight")

    best_cluster = rfm.groupby("Cluster")["Monetary"].mean().idxmax()

    worst_cluster = rfm.groupby("Cluster")["Monetary"].mean().idxmin()

    st.success(f"Highest Value Cluster: {best_cluster}")

    st.warning(f"Lowest Value Cluster: {worst_cluster}")

    st.info("""
AI Recommendation

• Focus marketing on high value clusters  
• Retarget inactive customers  
• Offer loyalty rewards for frequent buyers  
""")

# =========================
# DATASET
# =========================

with tab5:

    st.dataframe(df.head(50))

# =========================
# REALTIME METRIC
# =========================

st.subheader("Live Customer Monitor")

placeholder = st.empty()

for i in range(5):

    placeholder.metric("Active Customers", len(rfm_filtered))

    time.sleep(1)