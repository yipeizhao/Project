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

rewire_prob = np.linspace(0.01,0.9,200)
result = []
for prob in rewire_prob:
    G1 = G.copy()
    G2 = ut.single_link_rewiring(G1,prob)
    result.append(cx.OdC(G2))
plt.plot(rewire_prob,result)