from math import log
import networkx as nx
def small_world_property(G):
    n = len(G.nodes)
    m = len(G.edges)
    Cr = m/(n*(n-1)/2)
    Lr = log(n)/log(m*2/n)
    C = nx.average_clustering(G)
    L = nx.average_shortest_path_length(G)
    if (C*Lr)/(L*Cr)>1:
        return True
    else:
        return False