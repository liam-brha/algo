import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

students = [{"name": "Liam", "colour": "Blue", "team": "No", "subject": "Maths", "sport": "Tennis", "hobby": "Chatting about tech", "cuisine": "Thai"},
{"name": "Raymond", "colour": "Lavender", "team": "Essendon", "Subject": "Algorithmics", "sport": "Table Tennis", "hobby": "Reading", "cuisine": "Japanese"},
{"name": "Ella", "colour": "Blue", "team": "Brisbane Lions", "subject": "Maths", "sport": "Netball", "hobby": "Music", "cuisine": "Italian"},
{"name": "Vivian", "colour": "Green", "team": "No", "subject": "Chemistry", "sport": "Formula 1", "hobby": "Reading", "cuisine": "Japanese"}]

# make the student nodes
for student in students:
    nx.set_node_attributes(G, student, name=student["name"])

for i, student in enumerate(students):
    others = students.copy()
    others.pop(i)
    for friend in others:
        G.add_edge(student["name"], friend["name"])

# display
pos = nx.shell_layout(G)
nx.draw(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, nx.get_edge_attributes(G, "weight"))
plt.show()
