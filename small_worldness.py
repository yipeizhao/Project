#Small worldness

import utilities as ut
from math import log
import matplotlib.pyplot as plt
import Complexity as cx

n = 50
use_all_m = False
sample_number = 500
method = "Cr"
measure_method = getattr(cx,method)

#   Generating random graphs
graphs, df = ut.random_networks(n, use_all_m, sample_number )
Cr_ratio = []
Lr_ratio = []
complexity = []
small_world_c_ratio = []
small_world_l_ratio = []
small_world_complexity = []

#   Calculating parameters for the graphs
for i in range(len(graphs)):
    m = df["Number_of_edges"][i]
    Cr = m / (n*(n-1)/2)
    Lr = log(n)/log(df["Average_degree"][i])
    c = df["Average_clustering"][i]
    l = df["Average_distance"][i]
    if (c*Lr)/(l*Cr) < 1:
        Cr_ratio.append(c/Cr)
        Lr_ratio.append(l/Lr)
        complexity.append(measure_method(graphs[i]))
    else:
        small_world_c_ratio.append(c/Cr)
        small_world_l_ratio.append(l/Lr)
        small_world_complexity.append(measure_method(graphs[i]))

#   Plotting the data
plt.figure()
plt.scatter(small_world_c_ratio,small_world_l_ratio,
            label = "Small world", marker = "x",
            c = small_world_complexity)
plt.scatter(Cr_ratio,Lr_ratio,c = complexity,label = "Random graphs", alpha = 0.7)

plt.xlabel("C/Cr");plt.ylabel("L/Lr")
plt.title(method + " " + "n = " + str(n))
plt.legend()
plt.colorbar()