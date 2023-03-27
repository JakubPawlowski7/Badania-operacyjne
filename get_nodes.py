from collections import defaultdict
from math import inf

def get_nodes_from_matrix(M):
    n = len(M)
    weight = [[] for i in range(n)]
    V = []
    G = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if M[i][j] >= 1:
                if i not in V:
                    V.append(i)
                G[i].append(j)
                weight[i].append(M[i][j])
            else:
                weight[i].append(inf)
    G = dict(G)
                
    
    return V, weight, G


def get_nodes_from_list(L):
    V = []
    X = [L]
    n = len(L)
    G = defaultdict(list)
    
    for i in X:
        for key, value in i.items():
            V.append(key)
    for x in L:
        for y in L.get(x):
            for z in y:
                G[x].append(z)
    del x
    del y
    del z
    weight = []
    for node in V:
        weights = {endnode:int(weight)
            for w in L.get(node, {})
            for endnode, weight in w.items()}
        weight.append([weights.get(endnode, inf) for endnode in V])
    G = dict(G)
    return V, weight, G

