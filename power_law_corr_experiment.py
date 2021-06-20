import networkx as nx
import utilities as ux
import matplotlib.pyplot as plt
import collections
from math import log
from scipy.stats import pearsonr

result = []
for i in range(50,150):
    for j in range(3,7):
        G = nx.barabasi_albert_graph(i,j)
        degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
        degreeCount = collections.Counter(degree_sequence)
        deg, cnt = zip(*degreeCount.items())
        deg = list(deg)
        cnt = list(cnt)

        log_deg = [log(item) for item in deg]
        log_cnt = [log(item) for item in cnt]

        corr,_ = pearsonr(log_deg,log_cnt)
        result.append(corr)