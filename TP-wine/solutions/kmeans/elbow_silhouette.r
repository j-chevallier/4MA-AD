fviz_nbclust(wine2[,-c(1,2)], FUNcluster=kmeans, method="silhouette") +
    ggtitle("Optional number of cluster with silhouette")