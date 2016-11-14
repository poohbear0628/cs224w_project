import cPickle

degreeCountFile = "degreeCount.p"
subRedditsListFile = "subredditList.p"

degreeCount = cPickle.load(open(degreeCountFile, "rb"))

subReddits = degreeCount.keys()
print len(subReddits)

cPickle.dump(subReddits, open(subRedditsListFile, "wb"))

