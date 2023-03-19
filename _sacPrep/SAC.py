import networkx as nx
import matplotlib.pyplot as plt

HabitatMap = nx.Graph()

HabitatMap.add_nodes_from(["A", "B", "C", "D"])
HabitatMap.add_edges_from([
    ("A", "B", { "weight": 10, "paths": ["forrest cover"]}),
    ("C", "D", { "weight": 5, "paths": ["tunnel"]})])

nx.set_node_attributes(HabitatMap, {
    "A": {"population": 100, "netYrChange": -50},
    "B": {"population": 150, "netYrChange": 50 },
    "C": {"population": 30, "netYrChange": 20},
    "D": {"population": 80, "netYrChange": -20}
})

# set up graph render
pos = nx.spring_layout(HabitatMap, seed=2023)
nx.draw(HabitatMap, pos, node_color="grey", edge_color="grey")

nx.draw_networkx_labels(HabitatMap, pos)
nx.draw_networkx_edge_labels(HabitatMap, pos, nx.get_edge_attributes(HabitatMap, "weight"))

plt.show()
