n_pixel_x = 300
n_pixel_y = 128

mars_image = clusters_pca.reshape((n_pixel_x, n_pixel_y))

plt.figure(figsize = (10,10))
plt.imshow(mars_image, interpolation="nearest", aspect="auto", cmap=cmap)
plt.show()