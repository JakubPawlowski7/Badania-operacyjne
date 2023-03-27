from collections import defaultdict
from math import inf

G1 = {0: [{1:2}, {2:1}, {3:4}, {4:4}],
     1: [{0:2}, {3:3}, {6:5}],
     2: [{0:2}, {3:7}, {4:8}, {5:2}],
     3: [{0:4}, {1:3}, {2:7}, {5:4}, {6:1}],
     4: [{0:3}, {2:1}, {5:3}],
     5: [{2:2}, {3:4}, {4:3}, {6:3}],
     6: [{1:5}, {3:6}, {5:3}]}

G = {0: [{1:5}],
     1: [{3:3}, {4:9}],
     2: [{0:3}, {1:-4}],
     3: [{4:3}, {5:2}],
     4: [{2:-1}, {5:-5}],
     5: [{0:9}, {2:8}]}

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
    weight = []
    for node in V:
        weights = {endnode:int(weight)
            for w in L.get(node, {})
            for endnode, weight in w.items()}
        weight.append([weights.get(endnode, inf) for endnode in V])
    G = dict(G)
    return V, weight, G

V, w, G = get_nodes_from_list(G1)
V1, w1, G1 = get_nodes_from_list(G)

