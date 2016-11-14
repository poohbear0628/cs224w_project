import csv, cPickle, definePath

directories = definePath.definePaths()

clusteringCoefficientFile = directories["clusteringCoefficientFile"]
logClusteringCoefficientFile = directories["logClusteringCoefficientFile"]
weightedClusteringCoefficientsFile = directories["weightedClusteringCoefficients"]

clusteringCoefficients = cPickle.load(open(clusteringCoefficientFile, "rb"))
logClusteringCoefficients = cPickle.load(open(logClusteringCoefficientFile, "rb"))

header_subreddit = "SubReddit_Name"
header_clusteringCoefficients = "Clustering_Coefficients"
header_logClusteringCoefficients = "Log_Clustering_Coefficients"

with open(weightedClusteringCoefficientsFile, 'w') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=[header_subreddit, header_clusteringCoefficients, header_logClusteringCoefficients])
    writer.writeheader()
    for subreddit in clusteringCoefficients:
        writer.writerow({header_subreddit: subreddit,
                         header_clusteringCoefficients: clusteringCoefficients[subreddit],
                         header_logClusteringCoefficients: logClusteringCoefficients[subreddit]})
