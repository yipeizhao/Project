import networkx as nx
import numpy as np
from math import cos,pi
def Cr(G,normalisation = True):
    adj_matrix = nx.adjacency_matrix(G)
    adj_matrix = adj_matrix.todense()
    eigenvalues, eigenvectors = np.linalg.eig(adj_matrix)
    r = max(eigenvalues)
    
    if normalisation == True:
        n = len(G.nodes)
        c_r = (r - 2*cos(pi/(n+1)))/(n-1-2*cos(pi/(n+1)))
        r = 4*c_r*(1-c_r)
    return r