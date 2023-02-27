plt.scatter(mars_pca[:,0], mars_pca[:,1], c=clusters_pca, s=1, linewidths=1, cmap=cmap)
plt.title("Individuals factor map - PCA")
plt.show()