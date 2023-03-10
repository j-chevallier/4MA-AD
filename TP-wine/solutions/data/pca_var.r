options(repr.plot.width = 10, repr.plot.height = 8)

wine2 = wine
wine2[,-c(1,2)] = scale(wine[,-c(1,2)], scale=T, center=T) #sc
acp = PCA(wine2, quali.sup=c(1,2), scale.unit = TRUE, graph=FALSE)

# Visualisation of explained variance and variables
ggarrange(
    fviz_eig(acp), 
    fviz_pca_var(acp,axes=c(1,2))
)