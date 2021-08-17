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
    path = nx.ring_of_cliques(n,2)
    path_edges = list(path.edges)
    path.remove_edge(path_edges[0][0],path_edges[0][1])
    clique = nx.gnm_random_graph(n,n**2/2)
    R = redundancy(G)
    I = mutual_info(G)
    R_p = redundancy(path)
    R_c = redundancy(clique)
    I_p = mutual_info(path)
    I_c = mutual_info(clique)
    MAr = 4*((R-R_p)/(R_c - R_p))*(1 - (R-R_p)/(R_c-R_p))
    MAi = 4*((I-I_c)/(I_p-I_c))*(1-(I-I_c)/(I_p-I_c))
    if normalisation == True:
        return MAr * MAi
    else:
        return R*I
    
graphs,df = ut.random_networks(12,True,50)
result = [];result1 = [];result2=[]
for G in graphs:
    n = len(G.nodes)
    path = nx.path_graph(n)
    path_edges = list(path.edges)
    clique = nx.gnm_random_graph(n,n**2/2)
    R = redundancy(G)
    I = mutual_info(G)
    R_p = redundancy(path)
    R_c = redundancy(clique)
    I_p = mutual_info(path)
    I_c = mutual_info(clique)
    MAr = 4*((R-R_p)/(R_c - R_p))*(1 - (R-R_p)/(R_c-R_p))
    MAi = 4*((I-I_c)/(I_p-I_c))*(1-(I-I_c)/(I_p-I_c))    
    MAri = 4 *((R-R_p)/(R_c - R_p))*((I-I_c)/(I_p-I_c))
    result.append(MAr*MAi)
    result1.append(MAri)
    result2.append(R*(1-I))
import matplotlib.pyplot as plt
plt.scatter(df["Number_of_edges"],result)
plt.scatter(df["Number_of_edges"],result1,marker = "x")