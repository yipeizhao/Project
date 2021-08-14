import utilities as ut
import pandas as pd
#from bus_network_remove_degree_2 import remove_degree_2
import matplotlib.pyplot as plt
import Complexity as cx
import networkx as nx
from math import log
index = ["dolphins","pdzbase","GBPT_train",
         "hamsterster","Roget","flight"]
load_file_path = ["real_networks/processed/"+item+".csv" for item in index]
df = [pd.read_csv(item) for item in load_file_path]
networks = [ut.df_to_network(item) for item in df]

index_bus = ["london","paris","berlin","sydney","detroit","beijing"]
load_file_path = ["bus/processed/"+item+"_bus.csv" for item in index_bus]
df_bus = [pd.read_csv(item) for item in load_file_path]
networks_bus = [ut.df_to_network(item) for item in df_bus]
load_file_path = ["real_networks/processed/modified_bus/m_"+item+".csv" for item in index_bus]
df_bus_m = [pd.read_csv(item) for item in load_file_path]
networks_bus_m = [ut.df_to_network(item) for item in df_bus_m]


complexity = [cx.OdC(G) for G in networks]
complexity_bus = [cx.OdC(G) for G in networks_bus]
complexity_bus_m = [cx.OdC(G) for G in networks_bus_m]
l = [3.35695,5.32609,7.24001,3.21689,4.07539,4.10324]
l_bus = [32.33804,47.63117,33.28404,36.13135,70.51257,27.89102]
#c = [nx.average_clustering(G) for G in networks]
#c_bus = [nx.average_clustering(G) for G in networks_bus]
l_bus_m = [nx.average_shortest_path_length(G) for G in networks_bus_m]
#c_bus_m = [nx.average_clustering(G) for G in networks_bus_m]

n = [len(item.nodes) for item in networks]
m = [len(item.edges) for item in networks]
lr = [log(item)/log(2*item1/item) for item,item1 in zip(n,m)]

n_bus = [len(item.nodes) for item in networks_bus]
m_bus = [len(item.edges) for item in networks_bus]
lr_bus = [log(item)/log(2*item1/item) for item,item1 in zip(n_bus,m_bus)]

n_bus_m = [len(item.nodes) for item in networks_bus_m]
m_bus_m = [len(item.edges) for item in networks_bus_m]
lr_bus_m = [log(item)/log(2*item1/item) for item,item1 in zip(n_bus_m,m_bus_m)]

L_ratio = [item/item1 for item,item1 in zip(l,lr)]
L_ratio_bus = [item/item1 for item,item1 in zip(l_bus,lr_bus)]
L_ratio_bus_m = [item/item1 for item,item1 in zip(l_bus_m,lr_bus_m)]

    
color= ["red","blue","green","orange","brown","cyan"]
for i in range(len(networks)):
    plt.scatter(L_ratio[i],complexity[i],color = color[i])
    plt.scatter(L_ratio_bus[i],complexity_bus[i],color = color[i],marker = "x")
    plt.scatter(L_ratio_bus_m[i],complexity_bus_m[i],color = color[i],marker = "^")
plt.xlabel("L/Lr")
plt.ylabel("complexity")
plt.legend()
