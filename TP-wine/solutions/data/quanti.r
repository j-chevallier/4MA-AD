options(repr.plot.width = 8, repr.plot.height = 8)

dt = melt(wine[,-c(1,2)]) #gathering all numeric variable
ggplot(dt) + 
    aes(x=variable, y=value) + 
    geom_boxplot(color=1:6, fill=1:6, alpha=.3)


# --- #


options(repr.plot.width = 8, repr.plot.height = 6)

grid.arrange(
    ggplot(melt(wine[,c(3,4,8)]), aes(x=variable, y=value, color=variable, fill=variable)) + geom_violin(alpha=.3),
    ggplot(melt(wine[,c(5,6)]),aes(x=variable, y=value, color=variable, fill=variable)) + geom_violin(alpha=.3),
    ncol=2
)