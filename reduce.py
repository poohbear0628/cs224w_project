# AUTHOR: Samuel Hansen
# ABOUT: Accepts a sorted stdout output containing the user, subreddit, month
# performed by python map.py | sort. Returns a dictionary with each user mapped 
# to tuples of the subreddits and months they commented in, for example: 
# {user1 : set((subreddit1, month1), (subreddit2, month1),
#  user2 : set((subreddit3, month3), (subreddit4, month1))}

import cPickle as pickle
import sys

previous_user = ""
all_users = {}

for line in sys.stdin:
    # Tokenize data into a list
    data = line.strip('\n').split('\t')
    # Remove whitespaces
    data = [x.strip(' ') for x in data]
    # Extract data items
    user = data[0]
    subreddit = data[1]
    month = data[2]

    # If current user matches previous user
    if (previous_user == user): 
        all_users[user].add((subreddit, month))
     
    # If current user does not match previous user
    else:
        all_users[user] = set([(subreddit, month)])
        previous_user = user

# print all_users
pickle.dump(all_users, open("save.p", "wb" ))