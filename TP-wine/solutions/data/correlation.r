M = cor(wine[,-c(1,2)])
corrplot(M, method="number", type="upper")