import networkx as nx

def generate(graphData="friends") -> nx.Graph: # type: ignore
    match graphData:
        case "friends":
            G = nx.Graph()
            G.add_edges_from([(1, 2, { "weight": 6 }), (1, 3, { "weight": 3 }), (3, 4, { "weight": 2 }), (2, 4, { "weight": 5 }), (1, 4, { "weight": 1 })])
            return G
        case "digraph":
            G = nx.DiGraph()
            G.add_edges_from([(4, 3), [4, 1], [2, 3], [2, 4], [3, 2], [5, 2], [6, 5], [5, 6], [6, 7]])
            return G

