fig, ax = plt.subplots(4, 2, figsize=(15,8))

for k in range(2, 10):
    '''
    Create KMeans instance for different number of clusters
    '''
    kmeans = KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=100, random_state=42)
    q, mod = divmod(k, 2)
    '''
    Create SilhouetteVisualizer instance with KMeans instance
    Fit the visualizer
    '''
    visualizer = SilhouetteVisualizer(kmeans, colors='yellowbrick', ax=ax[q-1][mod])
    visualizer.fit(mars_reduced)