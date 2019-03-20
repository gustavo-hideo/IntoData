# CLUSTER

library(tidyverse)
library(datasets)
library(cluster)


data <- state.x77



# Computing the distance matrix
distance <- dist(as.matrix(data))

# Clustering
hc <- hclust(distance)

# Plotting a dendogram
plot(hc)

# Scaling data (normalization)
data.scaled <- scale(data)

# dendogram with normalized data
distance <- dist(as.matrix(data.scaled))
hc <- hclust(distance)
plot(hc)

# dendogram without Area
data.scaled_noArea <- scale(data[,1:7])
distance <- dist(as.matrix(data.scaled_noArea))
hc <- hclust(distance)
plot(hc)

# dendogram only with Frost
data.scaled_Frost <- scale(data[,7])
distance <- dist(as.matrix(data.scaled_Frost))
hc <- hclust(distance)
plot(hc)



# K-means CLustering
clust <- kmeans(data.scaled, 3)   # k = 5
summary(clust)
# Centers of the clusters (mean values)
clust$centers
# Clusters
clust$cluster
# Within-cluster sum of squares
clust$withinss
# Total sum of squares across clusters
clust$tot.withinss

# Plotting k-means clusters
clusplot(data.scaled, clust$cluster, color = T, shaed = T, labels = 2, lines = 0)

# CHOOSING NUMBER OF K USING ELBOW METHOD
whit <- c()
k <- c()
for (i in 1:25) {
    clust <- kmeans(data.scaled, i)
    whit[[i]] <- clust$tot.withinss
    k[[i]] <- i
}

elbow <- cbind(k, whit) %>%
    data.frame()
plot(elbow)

clust <- kmeans(data.scaled, 5)
clust$cluster
clusplot(data.scaled, clust$cluster, color = T, shaed = T, labels = 2, lines = 0)



