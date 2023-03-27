from get_nodes import *
from graphs import *
from copy import deepcopy

def Dijkstra(G, type, s):
    if type == 'matrix':
        V, w, G = get_nodes_from_matrix(G)
    else:
        V, w, G = get_nodes_from_list(G)
    n = len(G)
    d = [inf for i in range(n)]
    p = [0 for i in range(n)]
    Q = deepcopy(V)
    Q.remove(s)
    u_last = s

    while Q:
        for u in Q and w[u_last]:
            if d[u_last] + w[u_last][u] < d[u]:
                d[u] = d[u_last] + w[u_last][u]
                p[u] = u_last

        indicator = inf
        for u in Q:
            if beta[u] < indicator:
                indicator = beta[u]
                u_last = u
        Q.remove(u_last)
    return d, p
print(Dijkstra(G, 'list', 0))