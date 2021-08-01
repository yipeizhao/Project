import Complexity as cx
import utilities as ut
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import igraph as ig
import networkx as nx
G = nx.barabasi_albert_graph(500,3)
#G_df  =  pd.read_csv("real_networks/mammalia-voles-bhp-trapping.csv")
#G = ut.df_to_network(G_df)

rewire_prob = np.linspace(0.01,0.99,100)
result = []
for prob in rewire_prob:
    flag = True
    while flag == True:
        temp_g = G.copy()
        ig_graph = ig.Graph.from_networkx(temp_g)
        ig_graph.rewire_edges(prob)
        if ig_graph.is_connected():
            flag = False   
    nx_g = ig.Graph.to_networkx(ig_graph)
    result.append(cx.Ce(nx_g))
plt.plot(rewire_prob,result)
plt.xlabel("Rewire probability")
plt.ylabel("Ce complexity")
plt.title("Real Graph rewire complexity")