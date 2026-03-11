from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def find_best_k(data):

    best_k = 2
    best_score = -1

    X = data[["Recency","Frequency","Monetary"]]

    for k in range(2,10):

        model = KMeans(n_clusters=k)

        labels = model.fit_predict(X)

        score = silhouette_score(X,labels)

        if score > best_score:
            best_score = score
            best_k = k

    return best_k