import utilities as ut
import networkx as nx
import Complexity as cx
import matplotlib.pyplot as plt
graphs,df = ut.random_networks(10,False,10)
c1est = [cx.C1est(g) for g in graphs]
mari = [cx.MAri(g) for g in graphs]
odc = [cx.OdC(g) for g in graphs]