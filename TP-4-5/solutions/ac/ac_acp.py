K = 6

cmap = plt.get_cmap('Set3', K)

# -- #

ac_ss = AgglomerativeClustering(n_clusters=K, compute_distances=True, linkage="ward")
clusters_ac_ss = ac_ss.fit_predict(mars_reduced_samples)

ac = AgglomerativeClustering(n_clusters=K, compute_distances=True, linkage="ward")
clusters_ac = ac.fit_predict(mars_reduced)

# -- #

# On the sub-sample
plt.subplot(1,2,1)
plt.scatter(mars_reduced_samples[:,0], mars_reduced_samples[:,1], c=clusters_ac_ss, s=1, linewidths=1, cmap=cmap)

# On the complete dataset
plt.subplot(1,2,2)
plt.scatter(mars_reduced[:,0], mars_reduced[:,1], c=clusters_ac, s=1, linewidths=1, cmap=cmap)

plt.tight_layout()
plt.show()