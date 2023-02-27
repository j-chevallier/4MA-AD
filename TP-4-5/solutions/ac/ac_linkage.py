plt.subplot(2,2,1)
linkage_matrix = sch.linkage(mars_reduced2_samples, method='single')
sch.dendrogram(linkage_matrix)
plt.title("Dendrogram with single linkage")

plt.subplot(2,2,2)
linkage_matrix = sch.linkage(mars_reduced2_samples, method='complete')
sch.dendrogram(linkage_matrix)
plt.title("Dendrogram with complete linkage")

plt.subplot(2,2,3)
linkage_matrix = sch.linkage(mars_reduced2_samples, method='average')
sch.dendrogram(linkage_matrix)
plt.title("Dendrogram with average linkage")

plt.subplot(2,2,4)
linkage_matrix = sch.linkage(mars_reduced2_samples, method='ward')
sch.dendrogram(linkage_matrix)
plt.title("Dendrogram with Ward linkage")

plt.tight_layout()
plt.show()