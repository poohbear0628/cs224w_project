import cPickle as pickle
import os
import itertools
import math

# the directory where all the monthly user data is stored
directory = "D:\\224w\\project\\month_user_data"
# file subredditData to where the edge list is saved
destination_file = "D:\\224w\\project\\reddit.txt"
# minimum threshold of an edge weight for the edge to exist
# set to 0 to get all edges
threshold = 0.001


def subreddit_from_filename(filename):
    return filename.split("-users.pkl")[0]


def edgeweight(sub1, sub2, subreddit_users):
    users1 = subreddit_users[sub1]
    users2 = subreddit_users[sub2]

    intersection_users = users1.intersection(users2)

    # shortcut out
    if len(intersection_users) == 0:
        return 0

    union_users = users1.union(users2)
    return float(len(intersection_users))/len(union_users)


def read_files(directory):
    print "Reading files"
    subreddit_users = {}
    for filename in os.listdir(directory):
        sub_name = subreddit_from_filename(filename)
        print "Reading {}".format(sub_name)
        path = os.path.join(directory, filename)
        data = pickle.load(open(path, "rb"))

        # union all the users for every month for a year+ representation
        subreddit_users[sub_name] = set.union(*data)

    return subreddit_users


def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def write_edgelist(subreddit_users, filename):
    print "Writing edge list"
    count = 0
    written = 0
    total = nCr(len(subreddit_users), 2)
    with open(filename, "w") as output_file:
        output_file.write("# FromSubReddit\tToSubReddit\tEdgeWeight\r\n")
        for subreddit_pair in itertools.combinations(subreddit_users, 2):
            count += 1
            sub1 = subreddit_pair[0]
            sub2 = subreddit_pair[1]
            weight = edgeweight(sub1, sub2, subreddit_users)

            if weight > threshold:
                print "Writing edge {}/{}".format(count, total)
                output_file.write("{}\t{}\t{}\r\n".format(sub1, sub2, weight))
                written += 1

        output_file.write("# {} edges".format(written))

data = read_files(directory)
write_edgelist(data, destination_file)
