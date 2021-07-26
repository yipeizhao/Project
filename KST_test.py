import networkx as nx
from math import log
import collections
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from scipy.optimize import curve_fit
def ln(x):
    if x ==0:
        return 0
    else:
        return log(x)

def pl(x,a,b):
    return a*np.power(x,b)


G = nx.gnm_random_graph(100,2000)
degree_sequence = sorted([d for n, d in G.degree()])
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())
deg = list(deg)
cnt = list(cnt)
cnt = list(cnt)
cu_cnt = []
for i in range(len(cnt)):
    cu_cnt.append(sum(cnt[0:i+1]))
cu_cnt = [item/len(G.nodes) for item in cu_cnt]
pars,cov = curve_fit(f = pl,xdata=deg,ydata=cnt,p0 = [1,-2],bounds = (-np.inf,np.inf))
xlin = np.linspace(min(deg),max(deg),1000)
ylin = [pl(item,pars[0],pars[1]) for item in xlin]
ylin_cu_cnt = []
for i in range(len(ylin)):
    ylin_cu_cnt.append(sum(ylin[0:i+1]))
ylin_cu_cnt = [item/max(ylin_cu_cnt) for item in ylin_cu_cnt]
plt.plot(deg,cnt,label ="Degree dist")
plt.plot(xlin,ylin,color="red",label="Power law dist")
plt.legend()
log_deg = [ln(item) for item in deg]
log_cnt = [ln(item) for item in cu_cnt]
#plt.figure()
#plt.scatter(log_deg,log_cnt)
