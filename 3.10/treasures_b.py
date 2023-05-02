import networkx as nx
import matplotlib.pyplot as plt

a=nx.DiGraph()
a.add_nodes_from([("i", { "treasure": True }), ("c", { "treasure": True })])
a.add_edges_from([('S','d'),('d','b'), ('b','a'),('b','c')])
a.add_edges_from([('S','e'),('e','f'),('e','g'),('f','h'),('h','j'),('j','i')])

pos = nx.planar_layout(a)

# nodes
nx.draw_networkx_nodes(a, pos, node_size=300, node_color='lightgrey')
nx.draw_networkx_labels(a,pos,font_color = 'blue')

# edges
nx.draw_networkx_edges(a, pos, width=4, edge_color ='red')

treasures = { "x": 0, "treasures": 2, "tNodes": [] }

def DFS_r(G: nx.Graph, v):
    nx.set_node_attributes(G, { v: { "visited": True } })

    for u in [*G.neighbors(v)]:
        if not u in [*nx.get_node_attributes(G, "visited")]:
            if treasures["x"] == treasures["treasures"]:
                return
            elif u in [*nx.get_node_attributes(G, "treasure")]:
                treasures["x"] += 1
                treasures["tNodes"].append(u)
            DFS_r(G, u)

DFS_r(a, "S")
print(treasures)

plt.axis("off")
plt.show()

