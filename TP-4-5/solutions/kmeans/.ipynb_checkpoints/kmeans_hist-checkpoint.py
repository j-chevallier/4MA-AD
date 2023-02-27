K = 6

kmeans_pca = KMeans(n_clusters=K, random_state=0)
clusters_pca = kmeans_pca.fit_predict(mars_reduced)

# ----- #

cmap = plt.get_cmap('Set3',K)
plt.bar(*np.unique(clusters_pca, return_counts=True), color=cmap.colors)
plt.ylabel("Frequency")
plt.show()