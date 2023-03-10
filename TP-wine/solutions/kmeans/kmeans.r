reskmeans = kmeans(wine2[,-c(1,2)], centers=3) 

fviz_cluster(reskmeans, data=wine[,-c(1,2)], ellipse.type="norm", labelsize=8, geom=c("point"))