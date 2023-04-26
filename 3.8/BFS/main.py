# BFS
import networkx as nx
from queue import PriorityQueue, Queue
from typing import Any, Union, TypeAlias

import displayGraph
import exampleGraphs as e

# uses priority queue with herustic function

def BFS(network: nx.Graph, start, target) -> list[Any]:
    nodesToVisit = PriorityQueue() # the queue of nodes to process
    nodesVisited = [] # nodes actually processed
    nodesConsidered = [] # nodes that were in queue at some point
    
    def putNode(n, weight) -> Any:
        # heuristic: ranked by weight
        nodesToVisit.put((weight, n))
        nodesConsidered.append(n)

    nodesToVisit.put((0, start))

    while nodesToVisit.empty() == False:
        nodesVisited.append(n := nodesToVisit.get())
        nEdges = list(network.edges(n, "weight")) # type: ignore

        for (newNode, weight) in [(newNode[1], newNode[2]) for newNode in nEdges]:
            if newNode == target:
                nodesVisited.append((weight, newNode))
                return nodesVisited
            elif not newNode in nodesConsidered:
                putNode(newNode, weight)
    else:
        raise Exception("Target node not found")

    

network = e.generate("weighted numbers")

print(BFS(network, "D", "J"))
displayGraph.render(network)
