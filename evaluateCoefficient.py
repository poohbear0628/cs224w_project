import cPickle, definePath

directories = definePath.definePaths()
clusteringCoefficientFile = directories["clusteringCoefficientFile"]

clusteringCoefficients = cPickle.load(open(clusteringCoefficientFile, "rb"))

maxClusteringCoefficients = float("-inf")
minClusteringCoefficients = float("inf")

for subreddit in clusteringCoefficients:
    if clusteringCoefficients[subreddit] < minClusteringCoefficients:
        minClusteringCoefficients = clusteringCoefficients[subreddit]
    if clusteringCoefficients[subreddit] > maxClusteringCoefficients:
        maxClusteringCoefficients = clusteringCoefficients[subreddit]

print "min", minClusteringCoefficients
print "max", maxClusteringCoefficients