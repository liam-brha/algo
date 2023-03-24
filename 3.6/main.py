# finds the MST of a given friend network
import networkx as nx
from queue import PriorityQueue
from typing import Any, Union, TypeAlias

import displayGraph
import exampleGraphs as e

def batchQueue(queue, items):
    for item in list(items):
        queue.put(item)

nodes = lambda graph: list(graph.nodes())

node: TypeAlias = Union[int, str]

def genMST(network: nx.Graph) -> nx.Graph:
    pNode: Any
    edgeQueue = PriorityQueue() # minimum priority queue
    addedNodes = []
    addedEdges: list[tuple[node, node, int]] = []

    def updateEdges(node):
        edgePairList = [(edge[2], edge) for edge in network.edges(node, "weight")] # type: ignore
        batchQueue(edgeQueue, edgePairList)

    pNode = nodes(network)[0]
    updateEdges(pNode)

    while not edgeQueue.empty():
        if not pNode in addedNodes:
            updateEdges(pNode)
            addedNodes.append(pNode)
        
        while True: # iterate until all edges processed
            if edgeQueue.empty():
                break
            
            nEdge = edgeQueue.get()
            if not (destinationNode := nEdge[1][1]) in addedNodes:
                addedEdges.append(nEdge[1])
                pNode = destinationNode
                break
    
    MST = nx.Graph()

    print(addedEdges)
    for edge in addedEdges:
        MST.add_edge(*edge[0:2], weight=edge[2])

    return MST


friendNetwork = e.generate()
MST = genMST(friendNetwork)

displayGraph.render(MST, friendNetwork)
