import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.newman_watts_strogatz_graph(1000,10,0)
c0 = nx.average_clustering(G)
d0 = nx.average_shortest_path_length(G)
p = np.linspace(0.001,0.1,20)
cp = []
dp = []
for rewiring_prob in p:
    temp_G = nx.watts_strogatz_graph(1000,10,rewiring_prob)
    cp.append(nx.average_clustering(temp_G))
    dp.append(nx.average_shortest_path_length(temp_G))

cp_1 = [item/c0 for item in cp]

dp_1 = [item/d0 for item in dp]
plt.scatter(p,cp_1,label = 'C')
plt.scatter(p,dp_1,label = 'D')
plt.legend()

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.watts_strogatz_graph(1000,10,0)
c0 = nx.average_clustering(G)
d0 = nx.average_shortest_path_length(G)
p = np.linspace(0.001,0.1,20)
cp = []
dp = []
for rewiring_prob in p:
    temp_G = nx.watts_strogatz_graph(1000,10,rewiring_prob)
    cp.append(nx.average_clustering(temp_G))
    dp.append(nx.average_shortest_path_length(temp_G))

cp_1 = [item/c0 for item in cp]
plt.figure()
dp_1 = [item/d0 for item in dp]
plt.scatter(p,cp_1,label = 'C')
plt.scatter(p,dp_1,label = 'D')
plt.legend()