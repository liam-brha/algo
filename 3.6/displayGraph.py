import networkx as nx
import matplotlib.pyplot as plt

def render(*graphs: nx.Graph):
    for i, G in enumerate(graphs):
        print(G)
        plt.figure(i + 1)
        pos = nx.shell_layout(G)
        nx.draw(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, nx.get_edge_attributes(G, "weight"))
        plt.show()
