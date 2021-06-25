#Small worldness

import utilities as ut
from math import log
import matplotlib.pyplot as plt
import Complexity as cx

n = 50
use_all_m = False
sample_number = 500
method = "Ce"
measure_method = getattr(cx,method)

graphs, df = ut.random_networks(n, use_all_m, sample_number )
Cr = [0]*len(graphs)
Lr = [0]*len(graphs)
for i in range(len(graphs)):
    m = df["Number_of_edges"][i]
    Cr[i] = m / (n*(n-1)/2)
    Lr[i] = log(n)/log(df["Average_degree"][i])
    
Cr_ratio = [c/cr for c,cr in zip(df["Average_clustering"],Cr)]
Lr_ratio = [l/lr for l,lr in zip(df["Average_distance"],Lr)]

complexity = [measure_method(graph) for graph in graphs]
plt.figure()
plt.scatter(Cr_ratio,Lr_ratio,c = complexity)
plt.xlabel("C/Cr");plt.ylabel("L/Lr")
plt.title(method + " " + "n = " + str(n))
plt.colorbar()