import networkx

filename = "D:\\224w\\project\\cs224w_project\\data\\reddit-top10.txt"
destination_file = "D:\\224w\\project\\cs224w_project\\data\\weighted-coefficients-reddit-top10.csv"

graph = networkx.read_weighted_edgelist(filename, delimiter="\t")

cluster_coefficients = networkx.clustering(graph, weight="weight")

with open(destination_file, "w") as output_file:
    output_file.write("SubReddit_Name,Clustering_Coefficients\n")

    for key, value in cluster_coefficients.iteritems():
        output_file.write("{},{}\n".format(key, value))
        