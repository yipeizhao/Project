# Lr generator
import networkx as nx
n = [62,161,365,874,994,3397]
m = [159,209,594,4003,3640,19230]
lr = [0]*6
for j in range(10):
    for i in range(len(lr)):
        flag = 0
        while flag == 0:
            G = nx.gnm_random_graph(n[i],m[i])
            if nx.is_connected(G):
                lr[i] = lr[i] + nx.average_shortest_path_length(G)

n_bus = [8653,10644,4316,22659,5683,9249]
m_bus = [12285,12309,5869,26720,5946,14058]
lr_bus = [0]*6
for j in range(10):
    for i in range(len(lr)):
        flag = 0
        while flag == 0:
            G = nx.gnm_random_graph(n[i],m[i])
            if nx.is_connected(G):
                lr_bus[i] = lr_bus[i] + nx.average_shortest_path_length(G)
                flag = 1