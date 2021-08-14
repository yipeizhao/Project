import networkx as nx
import random
import numpy as np
import Complexity as cx
import matplotlib.pyplot as plt
def pairwise_rewiring(G,prob):
    rewire_number = int(prob*len(G.edges))
    G1 = G.copy()
    c = 0 
    while c != rewire_number:
        edges = list(G1.edges())
        rewire_edges = random.sample(edges,2)
        source1 = rewire_edges[0][0]
        source2 = rewire_edges[1][0]
        target1 = rewire_edges[0][1]
        target2 = rewire_edges[1][1]
        if len(set([source1,source2,target1,target2]))==4:
            G1.remove_edge(source1,target1)
            G1.remove_edge(source2,target2)
            G1.add_edge(source1,target2)
            G1.add_edge(source2,target1)
            if nx.is_connected(G1):
                c = c+1
            else:
                G1.add_edge(source1,target1)
                G1.add_edge(source2,target2)
                G1.remove_edge(source1,target2)
                G1.remove_edge(source2,target1)
    return G1

G = nx.barabasi_albert_graph(100,3)
step_prob = 0.01
G1 = G.copy()
step_prob = 0.05
prob_list = np.linspace(0,1,int(1/step_prob))
sample = 10
sample = 10
result = [0]*len(prob_list)
for iter_n in range(sample):
    G1 = G.copy()
    for i in range(int(1/step_prob)):
        G2 = G1.copy()
        G1 = pairwise_rewiring(G2, step_prob)
        result[i] = result[i] + cx.OdC(G1)
result = [item/sample for item in result]