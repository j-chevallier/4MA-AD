#Cluster vs Quality
table(wine$Quality, reskmeans$cluster)

# --- #

#Cluster
ggarrange(
    fviz_pca(acp, col.ind=as.factor(reskmeans$cluster), geom = c("point"), axes=c(1,2)),
    fviz_pca_ind(acp,axes=c(1,2), geom=c("point"), habillage=wine$Quality)
)clust_vs_quality