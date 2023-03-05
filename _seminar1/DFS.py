import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(["a", "b", "c", "d", "e", "f", "g"])
G.add_edges_from([("a", "d"), ("a", "b"), ("a", "c"), ("a", "e"), ("e", "g"), ("g", "c"), ("d", "f"), ("d", "b"), ("f", "b")])

# bottom to top
stack = ["a", "b"]
vistedNodes = []

while len(stack) > 0:
    node = stack.pop(-1)
    if not node in vistedNodes:
        vistedNodes.append(node)
        stack = stack + [*G.neighbors(node)]

print(vistedNodes)