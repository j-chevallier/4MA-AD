# Elbow method used with total within sum of square as metric

fviz_nbclust(wine2[,-c(1,2)], FUNcluster=kmeans, method="wss") +
    ggtitle("Optional number of cluster according Elbow")