import networkx as nx
def Ce(G,normalisation = True):
    if not nx.is_connected(G):
        return 0

    E = 0
    nodes = list(G.nodes())
    n=len(nodes)
    for i in range(n):
        for j in range(i+1, n):
            E = E + 1/nx.shortest_path_length(G,nodes[i],nodes[j])
    E = E /((n)*(n-1)/2)
    if normalisation ==True:
        E_path = 0
        for i in range(1,n):
            E_path = E_path + (n)/i
        E_path = E_path *2/((n)*(n-1))
    Ce = 4*(E-E_path)/(1-E_path)*(1- (E-E_path)/(1-E_path))
    return Ce