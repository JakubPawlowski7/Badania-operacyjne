from math import inf
from typing import Dict, List
from get_nodes import *
from graphs import *


V, w, G = get_nodes_from_list(G)
print(V)
print('\n')
print(w)
print('\n')
print(G)


def Johnson(G, type, s):
    n = len(G)
    if type == 'matrix':
        V, w, G = get_nodes_from_matrix(G)
    elif type == 'list':
        V, w, G = get_nodes_from_list(G)
    return V, w, G
print(Johnson(G, 'list', 0))