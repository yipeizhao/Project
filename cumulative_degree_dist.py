import networkx as nx
import collections
import matplotlib.pyplot as plt
from math import log10
from scipy.stats import pearsonr
import utilities
import numpy as np

def log(x):
    if x == 0:
        return 0
    else:
        return log10(x)
    
G = nx.barabasi_albert_graph(1000,7)
# nx.draw(G)
degree_sequence = sorted([d for n, d in G.degree()])
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())
deg = list(deg)
cnt = list(cnt)
cu_deg = list(np.linspace(min(deg),max(deg),max(deg)-min(deg)+1))
cu_deg = [int(item) for item in cu_deg]
cu_cnt = [0]*len(cu_deg)

for i in range(len(cu_deg)):
    if cu_deg[i] in deg:
        if i == 0:
            cu_cnt[i] = cnt[i]
        else:
            cu_cnt[i] = cu_cnt[i-1]+cnt[deg.index(cu_deg[i])]
    else:
        cu_cnt[i] = cu_cnt[i-1]
#cu_cnt = [-1*item for item in cu_cnt]
plt.plot(cu_deg,cu_cnt)
log_cnt = [log(item) for item in cu_cnt]
log_deg = [log(item) for item in cu_deg]
plt.figure()
plt.scatter(log_deg,log_cnt)