import cPickle as pickle
import os
import definePath

directories = definePath.definePaths()

commonDirectory = directories["commonDirectory"]
userCommentHistoryDirectory = directories["userCommentHistoryDirectory"]

filename = os.listdir(os.path.join(commonDirectory, userCommentHistoryDirectory))[0]
userCommentHistory = pickle.load(open(os.path.join(commonDirectory, userCommentHistoryDirectory, filename), "rb"))
for key in userCommentHistory:
    print key