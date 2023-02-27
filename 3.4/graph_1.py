import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(range(1,7))
G.add_edges_from([(1, 2), (1, 5), (2, 3), (2, 5), (5, 4), (3, 4), (4, 6)])

pos = nx.kamada_kawai_layout(G)
nx.draw(G, pos=pos)
nx.draw_networkx_labels(G, pos=pos)
plt.show()
