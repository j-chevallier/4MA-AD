options(repr.plot.width = 10, repr.plot.height = 6)

ggarrange(
    fviz_pca_ind(acp,axes=c(1,2), geom=c("point"), habillage=wine$Type),
    fviz_pca_ind(acp,axes=c(1,2), geom=c("point"), habillage=wine$Quality)
)