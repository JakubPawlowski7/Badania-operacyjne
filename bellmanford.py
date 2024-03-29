from math import inf
from typing import Dict, List
from get_nodes import *
from graphs import *

def BellmanFord1(G, w, s, V):
    n = len(G)
    #if type == 'matrix':
    #    V, w, G = get_nodes_from_matrix(G)
    #elif type == 'list':
    #    V, w, G = get_nodes_from_list(G)
    d = [inf for i in range(n)]
    p = [-1 for i in range(n)]


    d[s] = 0
    
    m = len(V) - 1
    for i in range(m):
        for (u, v), w_uv in w.items():
            if d[v] > d[u] + w_uv:
                d[v] = d[u] + w_uv
                p[v] = p[u] + v
    return d, p

def BellmanFord(G, type, s):
    n = len(G)
    if type == 'matrix':
        V, w, G = get_nodes_from_matrix(G)
    elif type == 'list':                            #Inicjalizacja zmiennych
        V, w, G = get_nodes_from_list(G)            #Wszystko dokładnie tak jak w pseudokodzie
    d = [inf for i in range(n)]
    p = [-1 for i in range(n)]


    d[s] = 0                                        
    
    m = len(V) - 1                              #Jako że algorytm Bellmana-Forda działa dla |V| - 1 wierzchołków to należy wziać to pod uwagę
    for i in range(m):                          #
        for u in range(len(w)):
            for v in range(len(w)):
                if w[u][v] != inf:
                    if d[v] > d[u] + w[u][v]:
                        d[v] = d[u] + w[u][v]
                        p[v] = u
    for j in d:
        if j < 0:
            print('Negative cycle detected!')
            return None
    
    return d, p

print(BellmanFord(G2, 'list', 0))

