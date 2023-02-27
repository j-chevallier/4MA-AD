K = 6
n_pixel_x = 300
n_pixel_y = 128
cmap = plt.get_cmap('Set3', K)

# --- #

mars_image_kmeans = clusters_kmeans_sorted.reshape((n_pixel_x, n_pixel_y))
mars_image_gmm = clusters_gmm.reshape((n_pixel_x, n_pixel_y))

# --- #

plt.subplot(1,2,1)
plt.imshow(mars_image_kmeans, interpolation="nearest", aspect="auto", cmap=cmap)
plt.title("With the kmeans algorithm")

plt.subplot(1,2,2)
plt.imshow(mars_image_gmm, interpolation="nearest", aspect="auto", cmap=cmap)
plt.title("With the GMM algorithm")

diffPlot(clusters_gmm, clusters_kmeans_sorted)

plt.tight_layout()
plt.show()