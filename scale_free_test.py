import networkx as nx

import collections
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
def pl(x,a,b):
    return a*np.power(x,b)

def scale_free_test(G):
    degree_sequence = sorted([d for n, d in G.degree()],reverse = True)
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    deg = list(deg)
    cnt = list(cnt)
    if len(deg)>5:
        pars,cov = curve_fit(f = pl,xdata=deg,ydata=cnt,p0 = [1,-2],bounds = (-np.inf,np.inf))
    else:
        return False
    # xlin = np.linspace(min(deg),max(deg),len(deg))
    # ylin = [pars[0]*np.power(item,pars[1]) for item in xlin]
    # error = [abs(a-b) for a,b in zip(cnt[::-1],ylin)]
    
    if pars[1]>-3 and pars[1]<-2:
        return True
    else:
        return False