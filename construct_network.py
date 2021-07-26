import networkx as nx
def construct_network(edge_list):
    G=nx.Graph()
    for item in edge_list:
        G.add_edge(item[0],item[1])
    return G
