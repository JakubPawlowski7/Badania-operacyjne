import copy
import math
from math import inf
from collections import defaultdict
import numpy
from typing import Dict, List

L = {1:[(2,1), (6,1)], 2:[(1,1), (3,1), (4,1)], 3:[(2,1)], 4:[(2,1), (5,1), (6,1)], 5: [(4,1)], 6:[(1,1), (4,1)]}
L1 = {1:[{2:1}, {6:1}], 2:[{1:1}, {3:1}, {4:1}], 3:[{2:1}], 4:[{2:1}, {5:1}, {6:1}], 5: [{4:1}], 6:[{1:1}, {4:1}]}
graph = {'1': [{'2':'15'}, {'4':'7'}, {'5':'10'}],
    '2': [{'3':'9'}, {'4':'11'}, {'6':'9'}],
    '3': [{'5':'12'}, {'6':'7'}],
    '4': [{'5':'8'}, {'6':'14'}],
    '5': [{'6':'8'}]}

G = {0: [{1:2}, {2:1}, {3:4}, {4:4}],
     1: [{0:2}, {3:3}, {6:5}],
     2: [{0:2}, {3:7}, {4:8}, {5:2}],
     3: [{0:4}, {1:3}, {2:7}, {5:4}, {6:1}],
     4: [{0:3}, {2:1}, {5:3}],
     5: [{2:2}, {3:4}, {4:3}, {6:3}],
     6: [{1:5}, {3:6}, {5:3}]}

M =    [[  0,  15,   0,   7,  10,   0      ],
        [ 15,   0,   9,  11 ,   0 ,   9    ],
        [  0 ,   9 ,   0 ,   0 ,  12 ,   7 ],
        [  7 ,  11 ,   0 ,   0 ,   8 ,  14 ],
        [ 10 ,   0 ,        12 ,   8 ,   0 ,   8 ],
        [  0 ,   9 ,   7 ,  14 ,   8 ,   0 ]]

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
                weight[i].append(math.inf)
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
    for i in L:
        for j in L.get(i):
            for k in j:
                G[i].append(k)
    weight = []
    for node in V:
        weights = {endnode:int(weight)
            for w in L.get(node, {})
            for endnode, weight in w.items()}
        weight.append([weights.get(endnode, math.inf) for endnode in V])
    G = dict(G)
    return V, weight, G

V1, w1, G1 = get_nodes_from_list(G)
print(G1)
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

print(DPA(G, 0, 'list'))




