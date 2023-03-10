wine = read.table("wine.txt")
head(wine)

# --- #

wine$Quality = as.factor(wine$Quality)                   #conversion to factor
wine$Type = factor(wine$Type, labels=c("white", "red"))  #rename levels of type

head(wine)