import pandas as pd
import Complexity as cx
import utilities as ut
def remove_degree_2(G1):
    G= G1.copy()
    flag = 1
    while flag == 1:
        node_len = len(G.nodes)
        remove_list = []
        for node in list(G.nodes):
            if G.degree(node) == 2:
                remove_list.append(node)
        
        for node in remove_list:
            neighbors = tuple(G.neighbors(node))
            if len(neighbors) == 2:
                G.remove_node(node)
                G.add_edge(neighbors[0],neighbors[1])
        if node_len == len(G.nodes):
            flag =0
    return G

def load_network(city):
    file = "processed_networks/" + str(city) + "_bus_simple.csv" 
    df = pd.read_csv(file)
    G = ut.df_to_network(df)
    return G

london = load_network("london")
paris = load_network("paris")
berlin = load_network("berlin")
sydney = load_network("sydney")
detroit = load_network("detroit")
beijing = load_network("beijing")

london_modified = remove_degree_2(london) 
paris_modified = remove_degree_2(paris) 
berlin_modified = remove_degree_2(berlin) 
sydney_modified = remove_degree_2(sydney)
detroit_modified = remove_degree_2(detroit)
beijing_modified = remove_degree_2(beijing)



networks = [london_modified,paris_modified,
            berlin_modified,sydney_modified,
            detroit_modified,beijing_modified]
result = []
result = [cx.OdC(network) for network in networks]