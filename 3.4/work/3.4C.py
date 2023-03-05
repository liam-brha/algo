import networkx as nx
import matplotlib.pyplot as plt

G = nx.digraph()

nodeList = ["A", "B", "C", "D", "E", "F", "G", "H", "J"]

G.add_nodes_from(nodeList)
G.add_edges_from([
    ("a", "b", { "weight": 2}),
    ("a", "e", { "weight": 3}),
    ("e", "d", { "weight": 8}),
    ("d", "f", { "weight": 4}),
    ("d", "c", { "weight": 9}),
    ("f", "c", { "weight": 4}),
    ("c", "b", { "weight": 7}),
    ("f", "b", { "weight": 1})
])

# set up graph render
pos = nx.spring_layout(G, seed=2023)
nx.draw(G, pos, nodelist=["a", "f"], node_color="grey", edge_color="grey")

nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, nx.get_edge_attributes(G, "weight"))

# coloured nodes
nx.draw_networkx_nodes(G, pos, nodelist=["e", "d", "b", "c"], node_color=["blue", "blue", "red", "red"])

# coloured edges
nx.draw_networkx_edges(G, pos, edgelist=[("e", "d"), ("b", "c")], edge_color=["blue", "red"])

plt.show()
