import networkx as nx
import csv
from random import randint
import pandas as pd
import numpy as np
import collections
from math import log2
from scipy.stats import pearsonr
import scipy

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


def random_networks(n=7,use_all_m = True,sample_number = 50):
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
                    "Small_world","Power_law"]
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
    
    for i in range(len(graph_list)):
        if power_law_property(graph_list[i]):
            df["Power_law"][i] = 1
    return graph_list,df


def small_world_property(df):
    df_list = []
    df=df.sort_values(by=['Number_of_edges'])
    for i in range(0,len(df),5):
        df_list.append(df[i:i+5])
    
    for dfs in df_list:
        small_world_parameter = []
        avg_distance = np.mean(dfs['Average_distance'])
        avg_clustering = np.mean(dfs['Average_clustering'])
        for index,rows in dfs.iterrows():
            small_world_parameter.append((rows['Average_clustering']*avg_distance)/(rows['Average_distance']*avg_clustering))
        for i in range(len(small_world_parameter)):
            if small_world_parameter[i]>1:
                dfs.iloc[i]['Small_world']=1
    return pd.concat(df_list)
       
        

def power_law_property(G):
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    deg = list(deg)
    cnt = list(cnt)
    log_deg = []
    log_cnt = []
    for item in deg:
        log_deg.append(log2(item))
    for item in cnt:
        log_cnt.append(log2(item))
    if len(log_cnt)>2:
        corr,_ = pearsonr(log_deg,log_cnt)
    else:
        corr = 0
    if corr < -0.75:
        return True
    else:
        return False        
    
def subgraph_one_edge_deletion(G):
    subgraphs = []
    for edge in list(G.edges):
        temp_graph = nx.Graph(G)
        temp_graph.remove_edge(edge[0],edge[1])
        subgraphs.append(temp_graph)
    return subgraphs


def number_of_ST(G):
    L = nx.laplacian_matrix(G)
    L = L.todense()
    remove_i = randint(0,L.shape[0]-1)
    L = np.delete(L,remove_i,0)
    L = np.delete(L,remove_i,1)
    det = scipy.linalg.det(L)
    det = int(det)
    return det

def isomorphic_graphs(G):
    subgraphs = subgraph_one_edge_deletion(G)
    ST_result = []
    for graph in subgraphs:
        ST_result.append(number_of_ST(graph))
    unique_ST = []
    unique_subgraphs = []
    for i in range(len(subgraphs)):
        if ST_result[i] not in unique_ST:
            unique_subgraphs.append(subgraphs[i])
            unique_ST.append(ST_result[i])
    return unique_subgraphs



