from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def perform_clustering(rfm, n_clusters=4):

   
    features = rfm[["Recency", "Frequency", "Monetary"]]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # tạo model KMeans
    model = KMeans(n_clusters=n_clusters, random_state=42)

    # train model
    clusters = model.fit_predict(scaled_features)

    rfm["Cluster"] = clusters

    return rfm, model

def find_optimal_clusters(rfm, max_k=10):

    features = rfm[["Recency", "Frequency", "Monetary"]]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    inertia_values = []

    K = range(1, max_k + 1)

    for k in K:

        model = KMeans(n_clusters=k, random_state=42)

        model.fit(scaled_features)

        inertia_values.append(model.inertia_)

    # vẽ biểu đồ
    plt.figure(figsize=(8,5))
    plt.plot(K, inertia_values, marker="o")

    plt.xlabel("Number of clusters (k)")
    plt.ylabel("Inertia")

    plt.title("Elbow Method for Optimal k")

    plt.show()