import definePath, cPickle

directories = definePath.definePaths()
edgeListFile = directories["edgeListFile"]
degreeCountFile = directories["degreeCountFile"]

degreeCount = {}
counter = 0
with open(edgeListFile, 'r') as edgeList:
    for line in edgeList:
        items = line.split()
        if len(items) == 3:
            degreeCount[items[0]] = degreeCount.get(items[0], 0) + 1
            degreeCount[items[1]] = degreeCount.get(items[1], 0) + 1
            counter = counter + 1


cPickle.dump(degreeCount, open(degreeCountFile, "wb"))