import utilities as ut
import Complexity as cx
from complement_graph import complement_graph
import matplotlib.pyplot as plt
import networkx as nx

graphs,df = ut.random_networks(20,False,500)
df = df.sort_index()
c_graphs = [complement_graph(item) for item in graphs]
g_complexity = [cx.Cr(item) for item in graphs]
c_complexity = [cx.Cr(item) for item in c_graphs]
plt.scatter(g_complexity,c_complexity,c= df["Number_of_edges"])
plt.title("n = 20 method = Cr")
plt.xlabel("Original graph")
plt.ylabel("Complement")
plt.colorbar()