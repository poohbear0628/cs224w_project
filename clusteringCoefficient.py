import cPickle, math

edgeListFile = "reddit-0.07.txt"
degreeCountFile = "degreeCount.p"
bracketWFile = "bracketW.p"
subRedditsListFile = "subredditList.p"
clusteringCoefficientFile = "clusteringCoefficient.p"
logClusteringCoefficientFile = "logClusteringCoefficient.p"
degreeOneNodesFile = "degreeOneNodes.p"
connectionMapDirectory = "connection/"
pickleFileExtension = ".p"

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
                        additionResult = additionResult + \
                                         0.5 * (connectionMap_subReddit[items[0]] + connectionMap_subReddit[items[1]])
        if additionResult == 0:
            logClusteringCoefficients[subreddit] = float("-inf")
            clusteringCoefficients[subreddit] = 0.0
        else:
            logClusteringCoefficients[subreddit] = -math.log(degreeCount[subreddit]) \
                                                   - math.log(degreeCount[subreddit] - 1) \
                                                   - math.log(bracketW[subreddit]) \
                                                   + math.log(additionResult)
            clusteringCoefficients[subreddit] = math.exp(logClusteringCoefficients[subreddit])
    counter = counter + 1
    print counter, subreddit, logClusteringCoefficients[subreddit], clusteringCoefficients[subreddit]

cPickle.dump(degreeOneNodes, open(degreeOneNodesFile, "wb"))
cPickle.dump(logClusteringCoefficients, open(logClusteringCoefficientFile, "wb"))
cPickle.dump(clusteringCoefficients, open(clusteringCoefficientFile, "wb"))


