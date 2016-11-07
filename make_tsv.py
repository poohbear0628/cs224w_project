# AUTHOR: Sam Hansen
# ABOUT: This file reads in all the LIWC data and prints it to stdout.
# Use make_tsv.py > liwc_data.tsv to create a tsv file.  

import cPickle as pickle
import os

# Sam directory (uncomment as needed)
directory = "/Users/Sam/Desktop/fall_2016/CS_224W/project/data/liwc"
seperator = '\t'

# Read in all LIWC files 
# for i in range(2048):
for filename in os.listdir(directory):
    # filename = os.listdir(directory)[i]
    path = os.path.join(directory, filename)
    liwc_categories = pickle.load(open(path, "rb"))
    subRedditName = filename.split('-')[0]
    
    for category in liwc_categories:
        print subRedditName, seperator, category, seperator, liwc_categories[category]