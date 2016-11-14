import cPickle, random

edgeListFile = "reddit-0.07.txt"
connectionMapDirectory = "connection/"
subRedditsListFile = "subredditList.p"
pickleFileExtension = ".p"

subReddits = cPickle.load(open(subRedditsListFile, "rb"))

counter = 0
for subReddit in subReddits:
    counter = counter + 1
    print counter, subReddit
    connectionMap = {}
    with open(edgeListFile, 'r') as edgeList:
        for line in edgeList:
            items = line.split()
            if len(items) == 3:
                if items[0] == subReddit:
                    connectionMap[items[1]] = float(items[2])
                elif items[1] == subReddit:
                    connectionMap[items[0]] = float(items[2])
    cPickle.dump(connectionMap, open(connectionMapDirectory + subReddit + pickleFileExtension, "wb"))
