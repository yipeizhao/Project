from subgraph_two_edge_deletion import subgraph_two_edge_deletion
from scipy.linalg import eig
import networkx as nx
import utilities
from math import comb

def C2espec(G,normalisation =True):
    subgraphs = subgraph_two_edge_deletion(G)
    spectra = []
    mcu = len(G.nodes())**1.68-10
    for i in range(len(subgraphs)):
        L = nx.laplacian_matrix(subgraphs[i]).todense()
        A = nx.adjacency_matrix(subgraphs[i]).todense()
        L = L + A + A
        eig_values,_ = eig(L)
        spectra.append(max(eig_values.real))
    rounded_spectra = []
    for item in spectra:
        rounded_spectra.append(round(item,10))
        
    N2espec = len(set(rounded_spectra))
    if normalisation == False:
        return N2espec
    else:
        return (N2espec-1)/(comb(mcu,2)-1)
