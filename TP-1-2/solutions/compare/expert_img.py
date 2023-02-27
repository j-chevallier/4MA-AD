K = 6
n_pixel_x = 300
n_pixel_y = 128
cmap = plt.get_cmap('Set3', K)

mars_image_expert = clusters_expert.reshape((n_pixel_x, n_pixel_y))

plt.imshow(mars_image_expert, interpolation="nearest", aspect="auto", cmap=cmap)
plt.title("Experts ground truth")
plt.show()