import cPickle as pickle
import os, string, math
import definePath

startPosition = 6

directories = definePath.definePaths()
commonDirectory = directories["commonDirectory"]
monthlyUserDataDirectory = directories["monthlyUserDataDirectory"]
userCommentHistoryDirectory = directories["userCommentHistoryDirectory"]

separator = '\t'
eol_terminator = '\n'
pickle_file_prefix = "UserCommentHistory_"
pickle_file_extension = directories["pickleFileExtension"]

totalCharacters = len(string.printable)
chunckCount = 100
setLength = int(math.ceil(float(totalCharacters) / float(chunckCount)))

characterSets = [None] * chunckCount
for i in range(chunckCount):
    characterSets[i] = set(string.printable[i * setLength : (i + 1) * setLength])

for currentSet in range(startPosition, len(characterSets)):
    userCommentHistory = {}

    for filename in os.listdir(os.path.join(commonDirectory, monthlyUserDataDirectory)):
        subredditData = os.path.join(commonDirectory, monthlyUserDataDirectory, filename)
        userSets = pickle.load(open(subredditData, "rb"))
        subRedditName = filename.split('-')[0]

        for month in range(len(userSets)):
            for user in userSets[month]:
                if user[0] in characterSets[currentSet]:
                    if user in userCommentHistory:
                        userCommentHistory[user].append((month, subRedditName))
                    else:
                        userCommentHistory[user] = [(month, subRedditName)]

    outputFileName = os.path.join(commonDirectory, userCommentHistoryDirectory,
                                  pickle_file_prefix + str(currentSet) + pickle_file_extension)
    pickle.dump(userCommentHistory, open(outputFileName, "wb"))
    print currentSet, separator, string.printable[i * setLength : (i + 1) * setLength], separator, len(userCommentHistory)