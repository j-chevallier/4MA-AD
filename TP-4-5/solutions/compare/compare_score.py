print("-- Results for K-means --")
print("Fowlkes Mallows score: %f" % fowlkes_mallows_score(clusters_kmeans, clusters_expert))
print("Mutual Information   : %f" % normalized_mutual_info_score(clusters_kmeans, clusters_expert))

print()

print("-- Results for CAH --")
print("Fowlkes Mallows score: %f" % fowlkes_mallows_score(clusters_ac, clusters_expert))
print("Mutual Information   : %f" % normalized_mutual_info_score(clusters_ac, clusters_expert))

print()

print("-- Results for GMM --")
print("Fowlkes Mallows score: %f" % fowlkes_mallows_score(clusters_gmm, clusters_expert))
print("Mutual Information   : %f" % normalized_mutual_info_score(clusters_gmm, clusters_expert))