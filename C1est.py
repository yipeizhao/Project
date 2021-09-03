import numpy as np
import networkx as nx
import math
from random import randint
def C1est(G,normalisation = True):
    subgraphs = []
    dets = []
    for edge in list(G.edges):
        temp_graph = G.copy()
        temp_graph.remove_edge(edge[0],edge[1])
        subgraphs.append(temp_graph)
    for item in subgraphs:
        L = nx.laplacian_matrix(item)
        L = L.todense()
        remove_i = randint(0,L.shape[0]-1)
        L = np.delete(L,remove_i,0)
        L = np.delete(L,remove_i,1)
        sign ,det = np.linalg.slogdet(L)
        det = math.exp(det)
        det = int(det)
        if det not in dets:
            dets.append(det)
    n = len(G.nodes)
    mcu = n**1.68-10
    N1est = len(dets)
    if normalisation == False:
        return N1est
    else:
        return (N1est-1)/(mcu-1)
