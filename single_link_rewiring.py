import networkx as nx
import random
import utilities as ut
import Complexity as cx
import pandas as pd
# def single_link_rewiring(G,prob):
#     nodes = set(G.nodes())
#     for edge in list(G.edges()):
#         if random.random()<prob:
#             source = edge[0]
#             neighbor_nodes = set(G.neighbors(source))
#             rewire_node = random.choice(list(nodes - neighbor_nodes))
#             G.remove_edge(source,edge[1])
#             G.add_edge(source,rewire_node)
#     return G 


# G = nx.gnp_random_graph(10,0.3)
# G1 = single_link_rewiring(G,0.5)
# ut.plot_deg_dist(G1)

df = pd.read_csv("real_networks/processed/bitcoin.csv")
G = ut.df_to_network(df)
print(cx.OdC(G))
prob = 0.8


G1 = G.copy()
nodes = set(G.nodes())
for edge in list(G1.edges()):
    if random.random()<prob:
        source = edge[0]
        neighbor_nodes = list(G1.neighbors(source))
        neighbor_nodes.append(source)
        neighbor_nodes = set(neighbor_nodes)
        if len(nodes - neighbor_nodes) != 0:
            rewire_node = random.choice(list(nodes - neighbor_nodes))
            G1.remove_edge(source,edge[1])
            G1.add_edge(source,rewire_node)

G2 = ut.gcc(G1)