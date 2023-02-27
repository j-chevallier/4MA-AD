K = 2

kmeans_pca = KMeans(n_clusters=K, init='k-means++', n_init=10)
clusters_pca = kmeans_pca.fit_predict(mars_reduced)
mars_image = clusters_pca.reshape((n_pixel_x, n_pixel_y))

cmap = plt.get_cmap('Set3',K)
plt.figure(figsize = (10,10))
plt.imshow(mars_image, interpolation="nearest", aspect="auto", cmap=cmap)
plt.show()