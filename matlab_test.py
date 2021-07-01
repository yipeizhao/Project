import networkx as nx
import scipy.io
G = nx.gnm_random_graph(20,75)
L = nx.laplacian_matrix(G).todense()
A = nx.adjacency_matrix(G).todense()
L = L+A+A
scipy.io.savemat('test.mat',L)