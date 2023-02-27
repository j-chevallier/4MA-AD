K = 6
n_pixel_x = 300
n_pixel_y = 128
cmap = plt.get_cmap('Set3', K)

# --- #

gmm = GaussianMixture(n_components=K, n_init=3)
clusters_gmm = gmm.fit_predict(mars_reduced)

# --- #

plt.subplot(1,2,1)
plt.scatter(mars_reduced[:,0], mars_reduced[:,1], c=clusters_gmm, s=1, linewidths=1, cmap=cmap)

plt.subplot(1,2,2)
mars_image_gmm = clusters_gmm.reshape((n_pixel_x, n_pixel_y))
plt.imshow(mars_image_gmm, interpolation="nearest", aspect="auto", cmap=cmap)
plt.title("Image Segmentation usign GMM")

plt.tight_layout()
plt.show()