import networkx as nx
from typing import List

def generate(nNames=[*range(1, 5)]) -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(nNames)
    G.add_edges_from([(1, 2, { "weight": 6 }), (1, 3, { "weight": 3 }), (3, 4, { "weight": 2 }), (2, 4, { "weight": 5 }), (1, 4, { "weight": 1 })])
    return G
