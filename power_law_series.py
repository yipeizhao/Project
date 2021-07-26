import networkx as nx
from scipy import _lib
def power_law_series(n,gamma):
    n = int(n)
    sequence = nx.random_powerlaw_tree_sequence(n, gamma,tries=10000)
    return sequence