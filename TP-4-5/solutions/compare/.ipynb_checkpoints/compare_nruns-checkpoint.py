K = 6
n_run = 10

# --- #

fm = []
nmi = []
for i in range(n_run):
    clusters = KMeans(K).fit_predict(mars_reduced)
    fm.append(fowlkes_mallows_score(clusters, clusters_expert))
    nmi.append(normalized_mutual_info_score(clusters, clusters_expert))
fm = np.array(fm)
nmi = np.array(nmi)

# --- #

print("Results for K-means, applied on first three dimensions of PCA, over %i runs:" % n_run)
print(u"Fowlkes Mallows   : %f \u00B1 %f" % (fm.mean(), fm.std()))
print(u"Mutual Information: %f \u00B1 %f" % (nmi.mean(), nmi.std()))