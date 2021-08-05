import pandas as pd
import networkx as nx
import utilities as ut

df = pd.read_csv("real_networks/flight.csv")
G = ut.df_to_network(df)
G = ut.gcc(G)
edges = list(G.edges())
source = [item[0] for item in edges]
target = [item[1] for item in edges]
data = {"source":source,"target":target}
df = pd.DataFrame(data=data)
df.to_csv("real_networks/flight.csv",index=False)