import cPickle

edgeListFile = "reddit-0.07.txt"
degreeCountFile = "degreeCount.p"
bracketWFile = "bracketW.p"

bracketW = {}
counter = 0
with open(edgeListFile, 'r') as edgeList:
    for line in edgeList:
        items = line.split()
        if len(items) == 3:
            bracketW[items[0]] = bracketW.get(items[0], 0) + float(items[2])
            bracketW[items[1]] = bracketW.get(items[1], 0) + float(items[2])
            bracketW[items[1]] = bracketW.get(items[1], 0) + float(items[2])
            counter = counter + 1

degreeCount = cPickle.load(open(degreeCountFile, "rb"))

counter = 0
for subreddit in bracketW:
    bracketW[subreddit] = bracketW[subreddit] / float(degreeCount[subreddit])
    if degreeCount[subreddit] <= 1 or bracketW[subreddit] == 0:
        counter = counter + 1
        print subreddit, degreeCount[subreddit], bracketW[subreddit]

print counter

cPickle.dump(bracketW, open(bracketWFile, "wb"))