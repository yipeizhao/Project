import itertools
import networkx as nx



def complement_graph(G):
    edges = list(G.edges)
    nodes = list(G.nodes)
    product_list=[]
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)):
            product_list.append((nodes[i],nodes[j]))
    complement = list(set(product_list)-set(edges))
    new_G = nx.Graph()
    for item in complement:
        new_G.add_edge(item[0],item[1])
    if nx.is_connected(new_G):
        return new_G
    else:
        return None