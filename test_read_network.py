import snap

data_file = "D:\\224w\\project\\cs224w_project\\data\\reddit-complete.txt"

mapping = snap.TStrIntSH()
graph = snap.LoadEdgeListStr(snap.PUNGraph, data_file, 0, 1, mapping)

for edge in graph.Edges():
    source = mapping.GetKey(edge.GetSrcNId())
    dest = mapping.GetKey(edge.GetDstNId())
    print "{} {}".format(source, dest)
    # do more here to read from edge weights column
