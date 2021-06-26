import networkx as nx
import collections
import matplotlib.pyplot as plt
from math import log
from scipy.stats import pearsonr
import utilities
import numpy as np

G = nx.barabasi_albert_graph(100,5)
# nx.draw(G)
degree_sequence = sorted([d for n, d in G.degree()])
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())
deg = list(deg)
cnt = list(cnt)
cu_deg = list(np.linspace(1,max(deg),max(deg)))
cu_deg = [int(item) for item in cu_deg]
cu_cnt = [0]*max(deg)
for i in range(0,max(deg)):
    if i+1 in deg:
        if i == 0:
            cu_cnt[i] = cnt[i]
        else:
            cu_cnt[i] = cu_cnt[i-1]+cnt[deg.index(i+1)]
    else:
        cu_cnt[i] = cu_cnt[i-1]
        
log_deg = [log(item) for item in cu_deg]
log_cnt = [log(item) for item in cu_cnt]