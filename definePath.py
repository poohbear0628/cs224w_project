def definePaths():
    directory = "WeightedClusteringCoefficient_CompleteGraphTop10/"
    directories = {}
    directories["edgeListFile"] = directory + "edgeList.txt"
    directories["degreeCountFile"] = directory + "degreeCount.p"
    directories["bracketWFile"] = directory + "bracketW.p"
    directories["subRedditsListFile"] = directory + "subredditList.p"
    directories["clusteringCoefficientFile"] = directory + "clusteringCoefficient.p"
    directories["logClusteringCoefficientFile"] = directory + "logClusteringCoefficient.p"
    directories["degreeOneNodesFile"] = directory + "degreeOneNodes.p"
    directories["connectionMapDirectory"] = directory + "connection/"
    directories["pickleFileExtension"] = ".p"
    directories["weightedClusteringCoefficients"] = directory + "weightedClusteringCoefficients.csv"
    directories["commonDirectory"] = "data"
    directories["monthlyUserDataDirectory"] = "month_user_data"
    directories["userCommentHistoryDirectory"] = "user_comment_history"
    return directories