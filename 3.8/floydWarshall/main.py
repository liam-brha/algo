# finds the MST of a given friend network
import networkx as nx
from queue import PriorityQueue, Queue
from typing import Any, Union, TypeAlias

import displayGraph
import exampleGraphs as e

def floydWarshall(network: nx.Graph) -> dict[Any, dict[Any, bool]]:
    # initliase vairbales
    tm: dict[Any, dict[Any, bool]] = {}  # transitive matrix
    nodes = list(network.nodes())

    for node in nodes:
        # intilaise transitive matrix
        tm[node] = {sourceNode:False for sourceNode in nodes}
        # if itself
        tm[node][node] = True 
        # if a direct child
        for child in [edge[1] for edge in network.edges(node)]:
            tm[node][child] = True
    
    # add connections
    for kNode in tm.keys():
        for sourceNode, possibleNodes in tm.items():
            for node in possibleNodes.keys():
                # if can get to some node k from sourceNode
                # and can get from k to destinationNode node
                if tm[kNode][node] == True and possibleNodes[kNode] == True:
                    possibleNodes.update({ node: True })
    
    return tm


network = e.generate("digraph")

print(floydWarshall(network))
displayGraph.render(network)
