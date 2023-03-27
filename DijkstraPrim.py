import copy
import math
from math import inf
from collections import defaultdict
import numpy
from typing import Dict, List







V, w, G = get_nodes_from_list(G)
print(G)

def DPA(G: (List[list], dict), s: int, type: str) -> (list, float):
    if type == 'matrix':

        V, weight, G = get_nodes_from_matrix(G)
    elif type == 'list':
        
        V, weight, G = get_nodes_from_list(G)
    
    a = copy.deepcopy(weight)

    A = []
    suma = 0
    n = len(V)
    Q = copy.deepcopy(V)
    
    for u in V:
        alfa = []
        for i in range(n):
            alfa.append(0)
        beta = []
        for i in range(n):
            beta.append(math.inf)


    Q.remove(s)
    beta[s] = 0
    u_last = s
    

    while Q:
        for u in Q and G[u_last]:
            if a[u][u_last] < beta[u]:
                alfa[u] = u_last
                beta[u] = a[u][u_last]

        indicator = math.inf
        for u in Q:
            if beta[u] < indicator:
                indicator = beta[u]
                u_last = u

        Q.remove(u_last)


        A.append((alfa[u_last], u_last))

        suma += a[alfa[u_last]][u_last]

    return (A, suma)






