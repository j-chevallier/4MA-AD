K = 6
n_pixel_x = 300
n_pixel_y = 128

cmap = plt.get_cmap('Set3', K)
# clusters_ac = ac.fit_predict(mars_reduced)

plt.subplot(1,2,1)
plt.scatter(mars_reduced[:,0], mars_reduced[:,1], c=clusters_ac, s=1, linewidths=1, cmap=cmap)

plt.subplot(1,2,2)a
mars_image_ac = clusters_ac.reshape((n_pixel_x, n_pixel_y))
plt.imshow(mars_image_ac, interpolation="nearest", aspect="auto", cmap=cmap)
plt.title("Image Segmentation using CAH")

plt.tight_layout()
plt.show()