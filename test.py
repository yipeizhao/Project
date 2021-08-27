import networkx as nx
import Complexity as cx
import utilities as ut
from math import log
import numpy as np
import matplotlib.pyplot as plt
n = 7
m= 11
graphs = []
for i in range(500):
    g = nx.gnm_random_graph(n,m)
    if nx.is_connected(g):
        graphs.append(g)
    
logdidj = [m*ut.redundancy(item) for item in graphs]
min_logdidj = min(logdidj);max_logdidj = max(logdidj)
sort_logdidj = sorted(logdidj)

R_p = ut.redundancy(nx.path_graph(n))
R_c = ut.redundancy(nx.gnm_random_graph(n,n*(n-1)*0.5))
I_p = ut.mutual_info(nx.path_graph(n))
I_c = ut.mutual_info(nx.gnm_random_graph(n,n*(n-1)*0.5))

R_space = np.linspace(min_logdidj/m,max_logdidj/m,500)
I_space = [log(2*m)-item for item in R_space]
mari = [((item1-R_p)/(R_c - R_p))*((item2-I_c)/(I_p-I_c)) for item1,item2 in zip(R_space,I_space)]
actual = [cx.MAri(item) for item in graphs]

if 4*max(mari)>max(actual):
    print(True)

normalise = [item/(4*max(mari)) for item in actual]
plt.scatter(logdidj,actual)