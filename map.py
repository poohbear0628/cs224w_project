import cPickle as pickle
import os

# Charlie directory (uncomment as needed)
# directory = "C:\\Users\\chenye\\Documents\\School Work\\16 - 17 Autumn\\CS 224W\\Project\\month_user_data\\"

# Sam directory (uncomment as needed)
directory = "/Users/Sam/Desktop/fall_2016/CS_224W/project/data/month_user_data"
seperator = '\t'

for i in range(3):
# for filename in os.listdir(directory):
    filename = os.listdir(directory)[i]
    path = os.path.join(directory, filename)
    # print path
    userSets = pickle.load(open(path, "rb"))
    subRedditName = filename.split('-')[0]

    for month in range(len(userSets)):
        for user in userSets[month]:
        	print user, seperator, subRedditName, seperator, month