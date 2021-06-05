from networkx import nx
from math import log10
def MAg(G,normalisation = True):
    if not nx.is_connected(G):
        return 0
    nodes = list(G.nodes)
    node_degree = []
    for node in nodes:
        node_degree.append(G.degree(node))
    
    m = sum(node_degree)/2
    n = len(nodes)
    R = 0
    I = 0
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)):
            R = R + log10(node_degree[i]*node_degree[j])
            I = I + log10(2*m/(node_degree[i]*node_degree[j]))
    
    R = R/m
    I = I/m
    R_path = 2*(n-2)/(n-1)*log10(2)
    I_path = log10(n-1)-(n-3)/(n-1)*log10(2)
    R_clique = 2*log10(n-1)
    I_clique = log10(n/(n-1))
    
    if normalisation == False:
        return (R-R_path)*(I-I_clique)
    else:
        MA_R = 4*((R-R_path)/(R_clique-R_path))*(1-(R-R_path)/(R_clique-R_path))
        MA_I = 4*((I-I_clique)/(I_path-I_clique))*(1-(I-I_clique)/(I_path-I_clique))
        return MA_R*MA_I


