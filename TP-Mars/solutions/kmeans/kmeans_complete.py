K = 6

kmeans_full = KMeans(n_clusters=K, init='k-means++', n_init=10)
clusters_full = kmeans_full.fit_predict(mars_data)
mars_image = clusters_full.reshape((n_pixel_x, n_pixel_y))

cmap = plt.get_cmap('Set3',K)
plt.figure(figsize = (10,10))
plt.imshow(mars_image, interpolation="nearest", aspect="auto", cmap=cmap)
plt.show()