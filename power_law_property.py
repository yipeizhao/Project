import collections
from math import log2
from scipy.stats import pearsonr
def power_law_property(G):
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    deg = list(deg)
    cnt = list(cnt)
    log_deg = []
    log_cnt = []
    for item in deg:
        log_deg.append(log2(item))
    for item in cnt:
        log_cnt.append(log2(item))
    if len(log_cnt)>2:
        corr,_ = pearsonr(log_deg,log_cnt)
    else:
        corr = 0
    if abs(corr)>0.55:
        return True
    else:
        return False