plotIndex = np.random.randint(0, 255, 6)

for i in range(6):
    plt.subplot(2, 3, i+1)
    mars_image = mars_data[:,plotIndex[i]].reshape((n_pixel_x, n_pixel_y))
    plt.imshow(mars_image, interpolation="nearest", aspect="auto")
    plt.xlabel("V%i" % (plotIndex[i]+1))
    
plt.tight_layout()
plt.show()