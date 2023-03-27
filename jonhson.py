from math import inf
from typing import Dict, List
from get_nodes import *
from graphs import *
from bellmanford import *

V, w, G = get_nodes_from_list(G)
print(V)
print('\n')
print(w)
print('\n')
print(G)
def Johnson(G, type, w, s):
    #if type == 'matrix':
    #    V, w, G = get_nodes_from_matrix(G)
    #else:
    #    V, w, G = get_nodes_from_list(G)
    d, p = BellmanFord(G, type, s)

    modifiedGraph = [[0 for x in range(len(graph))] for y in
                    range(len(graph))]

    for i in range(len(d)):
        if d[i] >= 0:
            pass
        else:
            d.remove(i)
    for x in range(len(w)):
        for y in range(len(w)):
            if w[x][y] != inf:
                modifiedGraph[x][y] = w[x][y] + d[x] - d[y]
    print(modifiedGraph)

Johnson(G, 'list', w, 0)