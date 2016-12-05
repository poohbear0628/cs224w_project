import community.best_partition
import community.modularity
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

file_in = "data/reddit-top10.txt"
G = nx.read_weighted_edgelist(file_in)

# nx.draw(G) 
# print(G)
nx.transitivity(G)

# Find modularity
part = community.best_partition(G)
mod = community.modularity(part,G)

# Plot, color nodes using community structure
values = [part.get(node) for node in G.nodes()]
nx.draw_spring(G, cmap=plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
plt.show()