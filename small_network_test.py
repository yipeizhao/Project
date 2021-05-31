import networkx as nx
from OdC import OdC
import numpy as np
from Cr import Cr
import matplotlib.pyplot as plt
n= 7
m=np.linspace(1,21,21)
graph_list = []
for edge_number in m:
    edge_number = int(edge_number)
    for iteration in range(1000):
        graph_list.append(nx.gnm_random_graph(n,edge_number))


edge_number = []
complexity = []
for item in graph_list:
    edge_number.append(len(item.edges))
    complexity.append(Cr(item))

clean_edge_number = []
clean_complexity=[]
for i in range(len(complexity)):
    if not np.isnan(complexity[i]):
        clean_edge_number.append(edge_number[i])
        clean_complexity.append(complexity[i])
        
plt.scatter(clean_edge_number,clean_complexity)