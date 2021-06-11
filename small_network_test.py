import networkx as nx
from random import randint
import pandas as pd
import numpy as np

def small_network_test(n=7,use_all_m = True,sample_number = 50):
    #Create a list of list to store all the graphs
    graph_list = []
    #Max number of edges.
    #If sample number>m , we only take m number experiments
    #Sample number>m will cause inefficient creation of graphs.
    m = (n*(n-1))/2
    m = int(m)
    #Create a df to store relevant information
    column_names = ["Number_of_edges","Average_degree",
                    "Average_distance",
                    "Average_clustering",
                    "Small_world"]
    if use_all_m == True:
        zero_list = [float(0)]*(sample_number*(m+1))
        df = pd.DataFrame(columns = column_names)
        for item in column_names:
            df[item] = zero_list 
    else:
        zero_list = [float(0)]*(sample_number)
        df = pd.DataFrame(columns = column_names)
        for item in column_names:
            df[item] = zero_list 
    #Create graphs and store their information in the df
    
    count = 0
    if use_all_m == True:
        
        for i in range(m+1):
            for j in range(sample_number):
                temp_graph = nx.gnm_random_graph(n,i)
                if nx.is_connected(temp_graph):
                    graph_list.append(temp_graph)
                    df["Number_of_edges"][count] = i
                    df["Average_degree"][count] =  (2*i)/n
                    df["Average_clustering"][count] = nx.average_clustering(temp_graph)
                    df["Average_distance"][count] = nx.average_shortest_path_length(temp_graph)
                    count  +=1

    else:
        for i in range(sample_number):
            edge_number  = randint(0,m)
            temp_graph=nx.gnm_random_graph(n,edge_number)
            if nx.is_connected(temp_graph):
                graph_list.append(temp_graph)
                df["Number_of_edges"][count] = edge_number
                df["Average_degree"][count] =  (2*edge_number)/n
                df["Average_clustering"][count] = nx.average_clustering(temp_graph)
                df["Average_distance"][count] = nx.average_shortest_path_length(temp_graph)
                count +=1
    
    drop_list = np.linspace(len(graph_list),len(df)-1,len(df)-len(graph_list))
    df=df.drop(drop_list)
    
    return graph_list,df







