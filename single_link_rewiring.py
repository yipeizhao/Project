import networkx as nx
import random
import matplotlib.pyplot as plt
import Complexity as cx
import numpy as np
def single_link_rewiring(G,prob):
    G1 = G.copy()
    rewire_number = int(prob * len(G1.edges))
    for i in range(rewire_number):
        flag = 0
        while flag ==0:
            source = random.choice(list(G1.nodes()))
            neighbors = list(G1.neighbors(source))
            remove_neighbor = random.choice(neighbors)
            G1.remove_edge(source,remove_neighbor)
            if not nx.is_connected(G1):
                G1.add_edge(source,remove_neighbor)
                #print(nx.is_connected(G1))
            else:
                options = set(list(G1.nodes)) - set(list(G1.neighbors(source)))-set([source,remove_neighbor])
                rewire_to = random.choice(list(options))
                G1.add_edge(source,rewire_to)
                flag = 1
    return G1

G = nx.barabasi_albert_graph(100,3)
step_prob = 0.01
G1 = G.copy()
prob = np.linspace(0,1,100)
result = []
networks = []
for i in range(10):
    G = nx.barabasi_albert_graph(100,3)
    G1 = G.copy()
    single_result = []
    for i in range(100):
        G2 = G1.copy()
        G1 = single_link_rewiring(G2, step_prob)
        single_result.append(cx.Cr(G1))
        networks.append(G1)
    result.append(single_result)

avg_result = [0]*100
for i in range(len(prob)):
    for j in range(len(result)):
        avg_result[i] = avg_result[i] + result[j][i]
avg_result = [item/len(result) for item in avg_result]
plt.scatter(prob,avg_result)