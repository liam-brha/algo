from queue import PriorityQueue
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
pqueue = PriorityQueue()
stack = []
queue = deque(["queue"])

stack.append(0)
stack.pop()
print(queue.popleft())
queue.append("test")
# priority number, item. minimum priority queues
pqueue.put((1, { "name": "Liam", "name": "Alice"}))
G.add_edges_from([("a", "b", { "weight": 2})])

# list comprehension
x = [i**2 for i in range(0, 3)]

# dict comprehension
y = {i: index for index, i in enumerate(["keya", "keyb", "keyc"])}
print(y)

# set up graph render
pos = nx.spring_layout(G, seed=2023)
nx.draw(G, pos, node_color="grey", edge_color="grey")

nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, nx.get_edge_attributes(G, "weight"))

plt.show()
