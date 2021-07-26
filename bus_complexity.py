import pandas as pd
import networkx as nx
import Complexity as cx
import utilities as ut
import matplotlib.pyplot as plt


generate_data = False

if generate_data:
    london_bus = pd.read_csv("GBPT/processed/london_bus.csv")
    paris_bus = pd.read_csv("bus/processed/paris.csv")
    berlin_bus = pd.read_csv("bus/processed/berlin.csv")
    sydney_bus = pd.read_csv("bus/processed/sydney.csv")
    detroit_bus = pd.read_csv("bus/processed/detroit.csv")
    
    
    london = nx.Graph()
    paris = nx.Graph();berlin = nx.Graph()
    sydney = nx.Graph();detroit = nx.Graph()
    
    
    for index,row in london_bus.iterrows():
        london.add_edge(row["source"],row["target"])
    london = ut.gcc(london)
    for index,row in paris_bus.iterrows():
        paris.add_edge(row["source"],row["target"])
    paris = ut.gcc(paris)
    for index,row in berlin_bus.iterrows():
        berlin.add_edge(row["source"],row["target"])
    berlin = ut.gcc(berlin)
    for index,row in sydney_bus.iterrows():
        sydney.add_edge(row["source"],row["target"])
    sydney = ut.gcc(sydney)
    for index,row in detroit_bus.iterrows():
        detroit.add_edge(row["source"],row["target"])
    detroit = ut.gcc(detroit)
    
    network_template = pd.DataFrame(data = {
        "source":[],
        "target":[]
        })
    
    london_edges = list(london.edges())
    london_source = [source[0] for source in london_edges]
    london_target = [target[1] for target in london_edges]
    london_simple = network_template.copy()
    london_simple["source"] = london_source;london_simple["target"]=london_target
    london_simple.to_csv("processed_networks/london_bus_simple.csv",index=False)
    
    paris_edges = list(paris.edges())
    paris_source = [source[0] for source in paris_edges]
    paris_target = [target[1] for target in paris_edges]
    paris_simple = network_template.copy()
    paris_simple["source"] = paris_source;paris_simple["target"]=paris_target
    paris_simple.to_csv("processed_networks/paris_bus_simple.csv",index=False)
    
    berlin_edges = list(berlin.edges())
    berlin_source = [source[0] for source in berlin_edges]
    berlin_target = [target[1] for target in berlin_edges]
    berlin_simple = network_template.copy()
    berlin_simple["source"] = berlin_source;berlin_simple["target"]=berlin_target
    berlin_simple.to_csv("processed_networks/berlin_bus_simple.csv",index=False)
    
    sydney_edges = list(sydney.edges())
    sydney_source = [source[0] for source in sydney_edges]
    sydney_target = [target[1] for target in sydney_edges]
    sydney_simple = network_template.copy()
    sydney_simple["source"] = sydney_source;sydney_simple["target"]=sydney_target
    sydney_simple.to_csv("processed_networks/sydney_bus_simple.csv",index=False)
    
    detroit_edges = list(detroit.edges())
    detroit_source = [source[0] for source in detroit_edges]
    detroit_target = [target[1] for target in detroit_edges]
    detroit_simple = network_template.copy()
    detroit_simple["source"] = detroit_source;detroit_simple["target"]=detroit_target
    detroit_simple.to_csv("processed_networks/detroit_bus_simple.csv",index=False)
else:
    london_simple = pd.read_csv("processed_networks/london_bus_simple.csv")
    paris_simple = pd.read_csv("processed_networks/paris_bus_simple.csv")
    berlin_simple = pd.read_csv("processed_networks/berlin_bus_simple.csv")
    sydney_simple = pd.read_csv("processed_networks/sydney_bus_simple.csv")
    detroit_simple = pd.read_csv("processed_networks/detroit_bus_simple.csv")
    london = ut.df_to_network(london_simple)
    paris = ut.df_to_network(paris_simple)
    berlin = ut.df_to_network(berlin_simple)
    sydney = ut.df_to_network(sydney_simple)
    detroit = ut.df_to_network(detroit_simple)


london_bus_complexity = cx.OdC(london)
paris_bus_complexity = cx.OdC(paris)
berlin_bus_complexity = cx.OdC(berlin)
sydney_bus_complexity = cx.OdC(sydney)
detroit_bus_complexity = cx.OdC(detroit)

complexities = [london_bus_complexity,
                paris_bus_complexity,
                berlin_bus_complexity,
                sydney_bus_complexity,
                detroit_bus_complexity
                ]

complexity_table = {
    "Complexity" : [],
    "Clustering" : [],
    "Distance" : [],
    "Ratio" : []
    }
index = ["London","Paris","Berlin","Sydney","Detroit"]
complexity_table = pd.DataFrame(data = complexity_table)
complexity_table["Complexity"] = complexities
complexity_table.index = index

clustering = []
clustering.append(nx.average_clustering(london))
clustering.append(nx.average_clustering(paris))
clustering.append(nx.average_clustering(berlin))
clustering.append(nx.average_clustering(sydney))
clustering.append(nx.average_clustering(detroit))
complexity_table["Clustering"] = clustering

distance = [32.33804,47.63117,
           33.28404,36.13135,
           70.51257
    ]

complexity_table["Distance"] = distance
colors = ["red","blue","orange","black","green"]
ratio = [c/l for c,l in zip(clustering,distance)]
complexity_table["Ratio"] = ratio
for i in range(len(index)):
    plt.scatter(complexities[i],ratio[i],color = colors[i],label = index[i])
plt.legend()
plt.xlabel("Complexity")
plt.ylabel("C/L")

