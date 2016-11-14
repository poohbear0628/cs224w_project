import cPickle, math, definePath

directories = definePath.definePaths()
edgeListFile = directories["edgeListFile"]
degreeCountFile = directories["degreeCountFile"]
bracketWFile = directories["bracketWFile"]
subRedditsListFile = directories["subRedditsListFile"]
clusteringCoefficientFile = directories["clusteringCoefficientFile"]
logClusteringCoefficientFile = directories["logClusteringCoefficientFile"]
degreeOneNodesFile = directories["degreeOneNodesFile"]
connectionMapDirectory = directories["connectionMapDirectory"]
pickleFileExtension = directories["pickleFileExtension"]

bracketW = cPickle.load(open(bracketWFile, "rb"))
degreeCount = cPickle.load(open(degreeCountFile, "rb"))
subRedditsList = cPickle.load(open(subRedditsListFile, "rb"))

clusteringCoefficients = {}
logClusteringCoefficients = {}
degreeOneNodes = set()

counter = 0
for subreddit in subRedditsList:
    if degreeCount[subreddit] == 1:
        degreeOneNodes.add(subreddit)
        clusteringCoefficients[subreddit] = 1.0
        logClusteringCoefficients[subreddit] = 0.0
    else:
        connectionMap_subReddit = cPickle.load(open(connectionMapDirectory + subreddit + pickleFileExtension, "rb"))
        additionResult = 0.0
        with open(edgeListFile, 'r') as edgeList:
            for line in edgeList:
                items = line.split()
                if len(items) == 3:
                    if items[0] in connectionMap_subReddit and items[1] in connectionMap_subReddit:
                        additionResult += (connectionMap_subReddit[items[0]] + connectionMap_subReddit[items[1]]) / bracketW[subreddit]
        if additionResult == 0:
            logClusteringCoefficients[subreddit] = float("-inf")
            clusteringCoefficients[subreddit] = 0.0
        else:
            clusteringCoefficients[subreddit] = additionResult / (degreeCount[subreddit]) / (degreeCount[subreddit] - 1)
            logClusteringCoefficients[subreddit] = math.log(clusteringCoefficients[subreddit])
    counter += 1
    print counter, subreddit, logClusteringCoefficients[subreddit], clusteringCoefficients[subreddit]

cPickle.dump(degreeOneNodes, open(degreeOneNodesFile, "wb"))
cPickle.dump(logClusteringCoefficients, open(logClusteringCoefficientFile, "wb"))
cPickle.dump(clusteringCoefficients, open(clusteringCoefficientFile, "wb"))


