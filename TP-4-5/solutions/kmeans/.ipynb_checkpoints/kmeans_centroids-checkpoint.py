K = 6

x = np.arange(0, 255)
for i in range(K):
    plt.plot(x, np.mean(mars_data[clusters_pca == i], axis = 0), color=cmap.colors[i])
    
plt.xlabel("Wave length")
plt.ylabel("Measured value")
plt.show()