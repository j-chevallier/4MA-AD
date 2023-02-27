K = 6
n_pixel_x = 300
n_pixel_y = 128
cmap = plt.get_cmap('Set3', K)

# --- #

cm, clusters_kmeans_sorted = matchClasses(clusters_expert, clusters_kmeans)
cm, clusters_gmm_sorted = matchClasses(clusters_expert, clusters_gmm)
cm, clusters_ac_sorted = matchClasses(clusters_expert, clusters_ac)

mars_image_expert = clusters_expert.reshape((n_pixel_x, n_pixel_y))
mars_image_kmeans = clusters_kmeans_sorted.reshape((n_pixel_x, n_pixel_y))
mars_image_gmm = clusters_gmm_sorted.reshape((n_pixel_x, n_pixel_y))
mars_image_ac = clusters_ac_sorted.reshape((n_pixel_x, n_pixel_y))

# -- #

plt.subplot(2,2,1)
plt.imshow(mars_image_expert, interpolation="nearest", aspect="auto", cmap=cmap)
plt.title("Experts ground truth")

plt.subplot(2,2,2)
plt.imshow(mars_image_kmeans, interpolation="nearest", aspect="auto", cmap=cmap)
plt.title("With the kmeans algorithm")

plt.subplot(2,2,3)
plt.imshow(mars_image_gmm, interpolation="nearest", aspect="auto", cmap=cmap)
plt.title("With the GMM algorithm")

plt.subplot(2,2,4)
plt.imshow(mars_image_gmm, interpolation="nearest", aspect="auto", cmap=cmap)
plt.title("With the CAH algorithm")

plt.tight_layout()
plt.show()