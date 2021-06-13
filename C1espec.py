from utilities import subgraph_one_edge_deletion
from scipy.linalg import eig
import networkx as nx
from collections import Counter
def C1espec(G,normalisation =True):
    subgraphs = subgraph_one_edge_deletion(G)
    spectra = []
    mcu = len(G.nodes())**1.68-10
    for i in range(len(subgraphs)):
        L = nx.laplacian_matrix(subgraphs[i]).todense()
        A = nx.adjacency_matrix(subgraphs[i]).todense()
        L = L + A + A
        eig_values,_ = eig(L)
        spectra.append(max(eig_values.real))
                    
    N1espec = len(set(spectra))
    if normalisation == False:
        return N1espec
    else:
        return (N1espec-1)/(mcu-1)