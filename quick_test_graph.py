import networkx as nx
from Cr import Cr
from OdC import OdC
import csv


def quick_test_graph(random = False, n = 15 , m =80):
    if random == False:
        G = nx.Graph()
        f=open('edges.csv','r')
        Ef=csv.reader(f)
        next(f)
        E=[(row[0],row[1]) for row in Ef]
        G=nx.Graph()
        G.add_edges_from(E)
    else:
        G = nx.gnm_random_graph(n,m)
    return G
