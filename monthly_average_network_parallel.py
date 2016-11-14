import cPickle as pickle
import os
import itertools
import math
from multiprocessing import Manager, Pool

windows = True
# the directory where all the monthly user data is stored
if windows:
    directory = "D:\\224w\\project\\month_user_data"
else:
    directory = "/afs/.ir/users/v/i/vinwoo/224w/month_user_data"
# file subredditData to where the edge list is saved
if windows:
    destination_file = "D:\\224w\\project\\cs224w_project\\data\\reddit-monthly-average-complete-parallel.txt"
else:
    destination_file = "/afs/.ir/users/v/i/vinwoo/224w/reddit-monthly-average-complete-parallel.txt"


# minimum threshold of an edge weight for the edge to exist
# set to 0 to get all edges

# 0.0023 retains ~10% of all edges
threshold = 0.00231664661599

def subreddit_from_filename(filename):
    return filename.split("-users.pkl")[0]

# minor optimization by saving empty list
empty_list = [0]*13


def edgeweight(sub1, sub2):
    assert len(sub1) == len(sub2)
    month_count = len(sub1)

    intersection_users = []
    for users1_month, users2_month in itertools.izip(sub1, sub2):
        intersection_users.append(len(users1_month.intersection(users2_month)))

    # shortcut out
    if intersection_users == empty_list:
        return 0

    union_users = []
    for users1_month, users2_month in itertools.izip(sub1, sub2):
        union_users.append(len(users1_month.union(users2_month)))

    weight = 0
    for intersection_month, union_month in itertools.izip(intersection_users, union_users):
        weight += float(intersection_month)/union_month

    return weight/month_count


def read_files(directory):
    print "Reading files"
    subreddit_monthly_users = {}
    for filename in os.listdir(directory):
        sub_name = subreddit_from_filename(filename)
        print "Reading {}".format(sub_name)
        path = os.path.join(directory, filename)
        subreddit_monthly_users[sub_name] = pickle.load(open(path, "rb"))

    return subreddit_monthly_users


def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def write_row(subs):
    sub1 = subs[0]
    sub2 = subs[1]
    weight = edgeweight(subreddit_users[sub1], subreddit_users[sub2])
    queue.put((sub1, sub2, weight))


def write_edgelist(filename):
    print "Writing edge list"

    with open(filename, "w") as output_file:
        output_file.write("# FromSubReddit\tToSubReddit\tEdgeWeight\r\n")
        pool = Pool()
        pool.map_async(write_row, itertools.combinations(subreddit_users, 2))

        total = nCr(len(subreddit_users), 2)
        edge_count = 0
        while total > 0:
            (sub1, sub2, weight) = queue.get()
            if weight > threshold:
                output_file.write("{}\t{}\t{}\r\n".format(sub1, sub2, weight))
                edge_count += 1

            total -= 1
            if total % 100 == 0:
                print "{} edges left".format(total)
                output_file.flush()
                os.fsync(output_file.fileno())

        output_file.write("# Total edges: {}".format(edge_count))
        output_file.flush()
        os.fsync(output_file.fileno())

    print "Finished writing edges"

if __name__ == '__main__':
    m = Manager()
    queue = m.Queue()
    subreddit_users = read_files(directory)
    write_edgelist(destination_file)
