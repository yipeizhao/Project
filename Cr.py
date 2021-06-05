import networkx as nx
import numpy as np
from math import cos,pi
def Cr(G,normalisation = True):
    if not nx.is_connected(G):
        return 0
    adj_matrix = nx.adjacency_matrix(G)
    adj_matrix = adj_matrix.todense()
    eigenvalues, eigenvectors = np.linalg.eig(adj_matrix)
    r = max(eigenvalues)
    r = r.real
    if normalisation == True:
        n = len(G.nodes)
        c_r_numerator = r-2 * cos(pi/(n+1))
        c_r_denominator = n-1-2*cos(pi/(n+1))
        c_r = c_r_numerator/c_r_denominator
        Cr_complexity = 4*c_r*(1-c_r)
        return Cr_complexity
    else:
        return r
