from math import log
import utilities as ut
import networkx as nx

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

def MAg(G,normalisation = True):
    n = len(G.nodes)
    R = redundancy(G)
    I = mutual_info(G)
    R_p = 2*(n-2)/(n-1)*log(2)
    R_c = 2*log(n-1)
    I_p = log(n-1)-((n-3)/(n-1))*log(2)
    I_c = log((n)/(n-1))
    MAr = 4*((R-R_p)/(R_c - R_p))*(1 - (R-R_p)/(R_c-R_p))
    MAi = 4*((I-I_c)/(I_p-I_c))*(1-(I-I_c)/(I_p-I_c))
    if normalisation == True:
        return MAr * MAi
    else:
        return R*I

graphs,df = ut.random_networks(7,True,100)
result = [MAg(g) for g in graphs]

import matplotlib.pyplot as plt
plt.scatter(df["Number_of_edges"],result)