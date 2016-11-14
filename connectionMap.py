import cPickle, definePath

directories = definePath.definePaths()
edgeListFile = directories["edgeListFile"]
connectionMapDirectory = directories["connectionMapDirectory"]
subRedditsListFile = directories["subRedditsListFile"]
pickleFileExtension = directories["pickleFileExtension"]

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
                    assert items[1] not in connectionMap
                    connectionMap[items[1]] = float(items[2])
                elif items[1] == subReddit:
                    assert items[0] not in connectionMap
                    connectionMap[items[0]] = float(items[2])
    assert subReddit not in connectionMap
    cPickle.dump(connectionMap, open(connectionMapDirectory + subReddit + pickleFileExtension, "wb"))
