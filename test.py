import networkx as nx
import Complexity as cx
import utilities as ut
from math import log
import numpy as np
import matplotlib.pyplot as plt
n=7
graphs,df = ut.random_networks(n,True,50)
# R_p = ut.redundancy(nx.path_graph(n))
# I_p = ut.mutual_info(nx.path_graph(n))
# R_c = ut.redundancy(nx.gnm_random_graph(n,n*(n-1)/2))
# I_c = ut.mutual_info(nx.gnm_random_graph(n,n*(n-1)/2))


def mari(G):
    n = len(G.nodes)
    R = ut.redundancy(G)
    I = ut.mutual_info(G)
    R_p = 2*log(2)*(n-2)/(n-1)
    R_c = 2*log(n-1)
    I_P = log(n-1)-log(2)*(n-3)/(n-1)
    I_c = log(n/(n-1))
    m=len(G.edges)
    numerator_1 = (R-R_p)
    numerator_2 = (I-I_c)
    denominator = 0.25*(log(2*m)-I_c-R_p)**2
    return numerator_1*numerator_2/denominator


num1 = [];num2=[];result=[]
for i in range(len(graphs)):
    c= mari(graphs[i])
    result.append(c)
    
plt.scatter(df["Number_of_edges"],result,label = "mari");plt.ylim([0,1])
plt.scatter(df["Number_of_edges"],[cx.MAg(g) for g in graphs],color = "red",label = "mag");plt.ylim([0,1])
plt.legend()
plt.xlabel("no of edges")
plt.ylabel("complexity")
plt.title("n="+str(n))