import networkx as nx
import Complexity
from random import randint
def BA_random_graphs(n,sample_number):
    graphs = []
    number_of_edges = []
    for i in range(sample_number):
        m=randint(1,n-1)
        temp_graph = nx.barabasi_albert_graph(n,m)
    return graphs