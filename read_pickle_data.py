import cPickle as pickle
import os

directory = "D:\\224w\\project\\liwc"
dataset = []

for filename in os.listdir(directory):
    path = os.path.join(directory, filename)
    dataset.append(pickle.load(open(path, "rb")))

for data in dataset:
    print data
