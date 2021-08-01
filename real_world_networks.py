import pandas as pd
import networkx as nx
import utilities as ut
import matplotlib.pyplot as plt
import Complexity as cx
import collections
network_df = {
"clg_ms_df" : pd.read_csv("real_networks/CollegeMsg.csv"),
"tvshow_df" : pd.read_csv("real_networks/fbTvshow.csv"),
"euroroads_df" : pd.read_csv("real_networks/inf-Euroroads.csv"),
"mammalia_df" : pd.read_csv("real_networks/mammalia-voles-bhp-trapping.csv"),
"roget_df" : pd.read_csv("real_networks/Roget.csv")
    }
# clg_ms_df = pd.read_csv("real_networks/CollegeMsg.csv")
# tvshow_df = pd.read_csv("real_networks/fbTvshow.csv")
# euroroads_df = pd.read_csv("real_networks/inf-Euroroads.csv")
# mammalia_df = pd.read_csv("real_networks/mammalia-voles-bhp-trapping.csv")
# roget_df = pd.read_csv("real_networks/Roget.csv")

networks = []
for key,val in network_df.items():
    networks.append(ut.df_to_network(val))
networks = [ut.gcc(network) for network in networks]
csv_name = ["processed_networks/"+key+".csv" for key,val in network_df.items()]
c = 0
for key,val in network_df.items():
   val.to_csv(csv_name[c],index=False)
   c=c+1

distance = [3.10784,6.27591,18.37129,6.58113,4.66837]
clustering = [nx.average_clustering(g) for g in networks]
ratio1 = [c/l for c,l in zip(clustering,distance)]
complexities1 = [cx.Ce(g) for g in networks]
colors = ["red","blue","orange","black","green"]
for i in range(len(complexities1)):
    plt.scatter(complexities1[i],ratio1[i],color = colors[i],marker = "x")


# deg_list = [];cnt_list = []
# for G in networks:
#     degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
#     degreeCount = collections.Counter(degree_sequence)
#     deg, cnt = zip(*degreeCount.items())
#     deg_list.append(deg)
#     cnt_list.append(cnt)
# plt.figure()
# for i in range(len(deg_list)):
#     plt.scatter(deg_list[i],cnt_list[i],color = colors[i],
#                 label = list(network_df.keys())[i])