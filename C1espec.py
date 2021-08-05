from scipy.linalg import eig
import networkx as nx

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
    rounded_spectra = []
    for item in spectra:
        rounded_spectra.append(round(item,7))
        
    N1espec = len(set(rounded_spectra))
    if normalisation == False:
        return N1espec
    else:
        return (N1espec-1)/(mcu-1)
    
def subgraph_one_edge_deletion(G):
    subgraphs = []
    for edge in list(G.edges):
        temp_graph = nx.Graph(G)
        temp_graph.remove_edge(edge[0],edge[1])
        subgraphs.append(temp_graph)
    return subgraphs
