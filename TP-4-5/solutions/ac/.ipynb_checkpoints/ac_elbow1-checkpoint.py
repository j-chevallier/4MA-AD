ac = AgglomerativeClustering(linkage="ward", compute_distances=True)
clusters_ac = ac.fit_predict(mars_reduced_samples)

distances = ac.distances_

n_sizes = 20
x = np.arange(n_sizes, 0, -1)
y = ac.distances_[-n_sizes:]

plt.scatter(x, y)

plt.xlabel('Point indices')
plt.ylabel('Distances')
plt.title("Choice of the number of classes")
plt.show()