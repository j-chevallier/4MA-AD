grid.arrange(
    # For the Quality variable
    ggplot(wine, aes(x=Quality, y=..prop.., group=1, fill=factor(..x..), color=factor(..x..))) + geom_bar(alpha=.5),
    # For the Type variable
    ggplot(wine, aes(x=Type, y=..prop.., group=1, fill=factor(..x..), color=factor(..x..))) + geom_bar(alpha=.5),     
ncol=2
)