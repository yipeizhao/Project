from scipy.linalg import eig
import networkx as nx

def C1espec(G,normalisation =True):
    subgraphs = subgraph_one_edge_deletion(G)
    spectra = []
    #Upper bound
    mcu = len(G.nodes())**1.68-10
    for i in range(len(subgraphs)):
        #L = laplacian matrix
        # L+2A to convert negative 1s to positive 1
        L = nx.laplacian_matrix(subgraphs[i]).todense()
        A = nx.adjacency_matrix(subgraphs[i]).todense()
        L = L + A + A
        #find the max eig value of L
        eig_values,_ = eig(L)
        spectra.append(max(eig_values.real))
    rounded_spectra = []
    #Round all the spectras, taking only the first 7 sf.
    for item in spectra:
        rounded_spectra.append(round(item,7))
    #Find the number of unique spectra values
    # #of unique spectra values = number of non-isomorphic subgraphs
    N1espec = len(set(rounded_spectra))
    if normalisation == False:
        return N1espec
    else:
        return (N1espec-1)/(mcu-1)

#Find all subgraph caused by deleting one edge
def subgraph_one_edge_deletion(G):
    subgraphs = []
    for edge in list(G.edges):
        temp_graph = nx.Graph(G)
        temp_graph.remove_edge(edge[0],edge[1])
        subgraphs.append(temp_graph)
    return subgraphs
