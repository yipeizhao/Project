import networkx as nx

import scipy
import numpy as np
from random import randint

def subgraph_one_edge_deletion(G):
    subgraphs = []
    for edge in list(G.edges):
        temp_graph = nx.Graph(G)
        temp_graph.remove_edge(edge[0],edge[1])
        subgraphs.append(temp_graph)
    return subgraphs


def number_of_ST(G):
    L = nx.laplacian_matrix(G)
    L = L.todense()
    remove_i = randint(0,L.shape[0]-1)
    L = np.delete(L,remove_i,0)
    L = np.delete(L,remove_i,1)
    det = scipy.linalg.det(L)
    det = int(det)
    return det

def isomorphic_graphs(G,edge_deletion = 1):
    if edge_deletion == 1:
        subgraphs = subgraph_one_edge_deletion(G)
        ST_result = []
        for graph in subgraphs:
            ST_result.append(number_of_ST(graph))
        unique_ST = []
        unique_subgraphs = []
        for i in range(len(subgraphs)):
            if ST_result[i] not in unique_ST:
                unique_subgraphs.append(subgraphs[i])
                unique_ST.append(ST_result[i])
        return unique_subgraphs
