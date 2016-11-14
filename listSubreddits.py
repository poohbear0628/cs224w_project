import cPickle, definePath

directories = definePath.definePaths()
degreeCountFile = directories["degreeCountFile"]
subRedditsListFile = directories["subRedditsListFile"]

degreeCount = cPickle.load(open(degreeCountFile, "rb"))

subReddits = degreeCount.keys()
print len(subReddits)

cPickle.dump(subReddits, open(subRedditsListFile, "wb"))

