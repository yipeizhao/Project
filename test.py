import networkx as nx
from OdC import OdC
import csv

G = nx.Graph()
f=open('edges.csv','r')
Ef=csv.reader(f)
next(f)
E=[(row[0],row[1]) for row in Ef]
G=nx.Graph()
G.add_edges_from(E)
nx.draw(G)

G = nx.gnp_random_graph(100,0.3)
result=OdC(G,normalisation = False)