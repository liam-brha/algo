import networkx as nx
import matplotlib.pyplot as plt

a=nx.DiGraph()
a.add_nodes_from([("b", { "treasure": True })])
a.add_edges_from([('S','d'),('d','b'), ('b','a'),('b','c')])
a.add_edges_from([('S','e'),('e','f'),('e','g'),('f','h'),('h','j'),('j','i')])

pos = nx.planar_layout(a)

# nodes
nx.draw_networkx_nodes(a, pos, node_size=300, node_color='lightgrey')
nx.draw_networkx_labels(a,pos,font_color = 'blue')

# edges
nx.draw_networkx_edges(a, pos, width=4, edge_color ='red')

# amazingly slow algorithm
def DFS_r(G: nx.Graph, v):
    nx.set_node_attributes(G, { v: { "visited": True } })

    for u in [*G.neighbors(v)]:
        if not u in [*nx.get_node_attributes(G, "visited")]:
            if u in [*nx.get_node_attributes(G, "treasure")]:
                return u
            else:
                return DFS_r(G, u)

print(DFS_r(a, "S"))

plt.axis("off")
plt.show()

