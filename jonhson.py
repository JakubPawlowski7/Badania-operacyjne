from math import inf
from typing import Dict, List
from get_nodes import *
from graphs import *
from bellmanford import *


def Johnson(G, type, s):
    if type == 'matrix':
        V, w, G = get_nodes_from_matrix(G)
    else:
        V, w, G = get_nodes_from_list(G)
    d, p = BellmanFord(G, type, s)

    modifiedGraph = [[0 for x in range(len(graph))] for y in
                    range(len(graph))]

    for i in range(len(d)):
        if d[i] >= 0:
            pass
        else:
            d.remove(i)
    for u in range(len(w)):
        for v in range(len(w)):
            if w[u][v] != inf:
                modifiedGraph[u][v] = w[u][v] + d[u] - d[v]
    print(modifiedGraph)

Johnson(G, 'list', 0)