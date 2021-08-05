import utilities as ut
import pandas as pd
#from bus_network_remove_degree_2 import remove_degree_2
import matplotlib.pyplot as plt
import Complexity as cx
import networkx as nx
index = ["bitcoin","coauthorship","GBPT_train",
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
l = [3.57084,4.79803,7.24001,3.21689,4.07539,4.10324]
l_bus = [32.33804,47.63117,33.28404,36.13135,70.51257,27.89102]
c = [nx.average_clustering(G) for G in networks]
c_bus = [nx.average_clustering(G) for G in networks_bus]
l_bus_m = [nx.average_shortest_path_length(G) for G in networks_bus_m]
c_bus_m = [nx.average_clustering(G) for G in networks_bus_m]
# complexity_group = [];c_group = [];l_group=[];index_group = []
# for i in range(len(networks)):
#     complexity_group.append(complexity[i])
#     complexity_group.append(complexity_bus[i])
#     c_group.append(c[i])
#     c_group.append(c_bus[i])
#     l_group.append(l[i])
#     l_group.append(l_bus[i])
#     index_group.append(index[i])
#     index_group.append(index_bus[i])
    
color= ["red","blue","green","orange","brown","cyan"]
for i in range(len(networks)):
    plt.scatter(l[i],complexity[i],color = color[i])
    plt.scatter(l_bus[i],complexity_bus[i],color = color[i],marker = "x")
    plt.scatter(l_bus_m[i],complexity_bus_m[i],color = color[i],marker = "^")
plt.xlabel("Average distance")
plt.ylabel("complexity")
#plt.legend()