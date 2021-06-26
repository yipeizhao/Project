from scipy.stats import pearsonr
import collections
from math import log
def power_law_property(G):
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    deg = list(deg)
    cnt = list(cnt)
    log_deg = [log(item) for item in deg]
    cu_cnt = [0]*len(cnt)
    for i in range(len(cnt)):
        if i == 0:
            cu_cnt[0]=cnt[0]
        else:
            cu_cnt[i]=cu_cnt[i-1]+cnt[i]
    log_cu_cnt = [log(item) for item in cu_cnt]
    corr,_ = pearsonr(log_deg,log_cu_cnt)
    if corr < -0.9:
        return True
    else:
        return False
