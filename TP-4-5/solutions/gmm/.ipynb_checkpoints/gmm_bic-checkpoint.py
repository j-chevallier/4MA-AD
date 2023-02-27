k_max = 15

bic = []
for k in range(2, k_max):
    gmm = GaussianMixture(n_components=k, init_params='kmeans', n_init=3)
    gmm.fit(mars_reduced)
    bic.append(gmm.bic(mars_reduced))
bic = np.array(bic)

plt.scatter(range(2, k_max), bic)
plt.show()