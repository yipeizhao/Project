from math import log
import utilities as ut
import networkx as nx
import Complexity as cx
def mutual_info(G):
    edges = list(G.edges)
    m = len(edges)
    I = 0
    for item in edges:
        d0 = len(list(G.neighbors(item[0])))
        d1 = len(list(G.neighbors(item[1]))) 
        I = I + log(2*m/(d0*d1))
    return I/m

def redundancy(G):
    edges = list(G.edges)
    m = len(edges)
    R = 0
    for item in edges:
        d0 = len(list(G.neighbors(item[0])))
        d1 = len(list(G.neighbors(item[1]))) 
        R = R + log((d0*d1))
    return R/m

def MAri(G,normalisation = True):
    n = len(G.nodes)
    R = redundancy(G)
    I = mutual_info(G)
    R_p = 2*(n-2)/(n-1)*log(2)
    R_c = 2*log(n-1)
    I_p = log(n-1)-((n-3)/(n-1))*log(2)
    I_c = log((n)/(n-1))
    if normalisation == True:
        return 4 *((R-R_p)/(R_c - R_p))*((I-I_c)/(I_p-I_c))
    else:
        return R*I
n=7
R_p = 2*(n-2)/(n-1)*log(2)
R_c = 2*log(n-1)
I_p = log(n-1)-((n-3)/(n-1))*log(2)
I_c = log((n)/(n-1))
graphs,df = ut.random_networks(n,True,50)
result = [cx.MAg(g) for g in graphs]
red = [redundancy(g) for g in graphs]
red = [(item-R_p)/(R_c-R_p) for item in red]
mi = [mutual_info(g) for g in graphs]
mi = [(item-I_c)/(I_p-I_c) for item in mi]

import matplotlib.pyplot as plt
plt.scatter(df["Number_of_edges"],result);
