import networkx as nx
import random
from random import randint
import pandas as pd
import numpy as np
import collections
from scipy.stats import pearsonr
from itertools import combinations_with_replacement
import math
from math import log
import matplotlib.pyplot as plt

#   Generates a list of graphs and their corresponding parameter.
#   Notice the function will only return connected graphs, disconnected graphs
#   will not be returned. Thus the actual number of graphs returned will be less
#   than expected.
#   Parameters:
#   n: number of nodes
#   use_all_m: if this is true, then the function will generates samples using all
#   the edge numbers * sample_number
#   sample_number: number of samples for each edge if use_all_m = True
#   Otherwise the sample_number defines how many graphs will be returned in total
def random_networks(n=7,use_all_m = True,sample_number = 50):
    #   Create a list to record all the graphs
    graph_list = []
    #   Max number of edges.
    m = (n*(n-1))/2
    m = int(m)
    #   Create a df to store relevant information
    column_names = ["Number_of_edges","Average_degree",
                    "Average_distance",
                    "Average_clustering"]
    #   Filling the df with zeros
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
    #   Creating graphs using different parameters
    #   count record the actual number of graphs generated by the function
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
    df=df.sort_index()
    return graph_list,df
#   Return a list of subgraphs of the graph G by taking an edge off the graph
def subgraph_one_edge_deletion(G):
    subgraphs = []
    for edge in list(G.edges):
        temp_graph = G.copy()
        temp_graph.remove_edge(edge[0],edge[1])
        subgraphs.append(temp_graph)
    return subgraphs

#   Return the number of spanning trees of a graph.
#   This calculation is based on the Kirchhoffs theorem, which is:
#   number of ST = det(reduced Laplacian matrix)
#   A reduced Laplacian matrix is the Laplacian matrix with
#   a random row i and column i to be removed
def number_of_ST(G):
    L = nx.laplacian_matrix(G)
    L = L.todense()
    remove_i = randint(0,L.shape[0]-1)
    L = np.delete(L,remove_i,0)
    L = np.delete(L,remove_i,1)
    sign ,det = np.linalg.slogdet(L)
    det = sign * math.exp(det)
    det = int(det)
    return det

#   Return number of isomorphic subgraphs of a graph
#   After taking all the one-edge-deletion subgraphs,
#   investigates the number of different ST will remove isomorphic subgraphs
def isomorphic_graphs(G):
    subgraphs = subgraph_one_edge_deletion(G)
    ST_result = []
    for graph in subgraphs:
        ST_result.append(number_of_ST(graph))
    unique_ST = []
    unique_subgraphs = []
    ST_result = [str(item)[:10] for item in ST_result]
    for i in range(len(subgraphs)):
        if ST_result[i] not in unique_ST:
            unique_subgraphs.append(subgraphs[i])
            unique_ST.append(ST_result[i])
    return unique_ST

#   Generates a list of BA random graphs
#   Parameters:
#   n = number of nodes
#   sample_number = Number of samples
def BA_random_graphs(n,sample_number):
    graphs = []
    for i in range(sample_number):
        m=randint(1,n-1)
        temp_graph = nx.barabasi_albert_graph(n,m)
        if nx.is_connected(temp_graph):
            graphs.append(temp_graph)
    return graphs

#   Generates a list of WS random graphs
#   Parameters:
#   n = number of nodes
#   sample_number = Number of samples
def WS_random_graphs(n,sample_number):
    graphs = []
    for i in range(sample_number):
        p= random.uniform(0.001,0.1)
        k= random.randint(2,n)
        graphs.append(nx.watts_strogatz_graph(n,k,p))
    return graphs

#   Generates a list of NS random graphs
#   Parameters:
#   n = number of nodes
#   sample_number = Number of samples
def NW_random_graphs(n,sample_number):
    graphs = []
    for i in range(sample_number):
        p= random.uniform(0.001,0.1)
        k= random.randint(2,n)
        graphs.append(nx.newman_watts_strogatz_graph(n,k,p))
    return graphs

#   Return a list of subgraphs by taking two edges off from the graph
def subgraph_two_edge_deletion(G):
    subgraphs = []
    remove_edges = np.linspace(0,len(G.edges)-1,len(G.edges))
    remove_edge_product = combinations_with_replacement(remove_edges,2)
    remove_edge_tuple = []
    for x in remove_edge_product:
        remove_edge_tuple.append(x)
    remove_edge_final = []
    for i in range(len(remove_edge_tuple)):
        if remove_edge_tuple[i][0]!= remove_edge_tuple[i][1]:
            remove_edge_final.append(remove_edge_tuple[i])
    subgraphs = []
    edge_list = list(G.edges)
    for i in range(len(remove_edge_final)):
        temp_graph = nx.Graph(G)
        edge1 = remove_edge_final[i][0]
        edge1 = int(edge1)
        edge2 = remove_edge_final[i][1]
        edge2 = int(edge2)
        edge1_loc = edge_list[edge1]
        edge2_loc = edge_list[edge2]
        temp_graph.remove_edge(edge1_loc[0],edge1_loc[1])
        temp_graph.remove_edge(edge2_loc[0],edge2_loc[1])
        subgraphs.append(temp_graph)
    return subgraphs

#   Check whether a network is empty(no edges)
def empty_check(G):
    if len(G.nodes()) == 0 or len(G.edges())==0:
        return True
    else:
        return False

#   Convert a dataframe to a network
def df_to_network(df):
    source = [row[0] for index,row in df.iterrows()]
    target = [row[1] for index,row in df.iterrows()]
    G = nx.Graph()
    [G.add_edge(item1,item2) for item1,item2 in zip(source,target)]
    return G

#   Finding the giant component of a network
def gcc(G):
    Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
    G0 = G.subgraph(Gcc[0])
    return G0

#    Plotting the degree distribution of a graph
def plot_deg_dist(G):
    degree_sequence = sorted([d for n, d in G.degree()],reverse = True)
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    deg = list(deg)
    cnt = list(cnt)
    plt.bar(deg,cnt)
    return 0

#   Convert a NetworkX graph object to a dataframe
def network_to_df(G):
    edges = list(G.edges())
    source = [item[0] for item in edges]
    target = [item[1] for item in edges]
    df = pd.DataFrame(data = {"source":source,"target":target})
    return df

#   Rewire the network G with given probability prob,using pairwise rewiring
def pairwise_rewiring(G,prob):
    rewire_number = int(prob*len(G.edges))
    G1 = G.copy()
    c = 0 
    while c != rewire_number:
        edges = list(G1.edges())
        rewire_edges = random.sample(edges,2)
        source1 = rewire_edges[0][0]
        source2 = rewire_edges[1][0]
        target1 = rewire_edges[0][1]
        target2 = rewire_edges[1][1]
        if len(set([source1,source2,target1,target2]))==4:
            if not G1.has_edge(source1,target2) and not G1.has_edge(source2,target1):
                G1.remove_edge(source1,target1)
                G1.remove_edge(source2,target2)
                G1.add_edge(source1,target2)
                G1.add_edge(source2,target1)
                if nx.is_connected(G1):
                    c = c+1
                else:
                    G1.add_edge(source1,target1)
                    G1.add_edge(source2,target2)
                    G1.remove_edge(source1,target2)
                    G1.remove_edge(source2,target1)
    return G1

#   Rewire the network G with given probability prob,using single link rewiring
def single_link_rewiring(G,prob):
    G1 = G.copy()
    rewire_number = int(prob * len(G1.edges))
    for i in range(rewire_number):
        flag = 0
        while flag ==0:
            source = random.choice(list(G1.nodes()))
            neighbors = list(G1.neighbors(source))
            remove_neighbor = random.choice(neighbors)
            G1.remove_edge(source,remove_neighbor)
            if not nx.is_connected(G1):
                G1.add_edge(source,remove_neighbor)
            else:
                options = set(list(G1.nodes)) - set(list(G1.neighbors(source)))-set([source,remove_neighbor])
                rewire_to = random.choice(list(options))
                G1.add_edge(source,rewire_to)
                flag = 1
    return G1

#   Calculates the mutual information of a graph
def mutual_info(G):
    edges = list(G.edges)
    m = len(edges)
    I = 0
    for item in edges:
        d0 = len(list(G.neighbors(item[0])))
        d1 = len(list(G.neighbors(item[1]))) 
        I = I + log(2*m/(d0*d1))
    return I/m

#   Calculates the redundancy of a graph
def redundancy(G):
    edges = list(G.edges)
    m = len(edges)
    R = 0
    for item in edges:
        d0 = len(list(G.neighbors(item[0])))
        d1 = len(list(G.neighbors(item[1]))) 
        R = R + log((d0*d1))
    return R/m

#   Return the complement of a graph
def complement_graph(G):
    edges = list(G.edges)
    nodes = list(G.nodes)
    product_list=[]
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)):
            product_list.append((nodes[i],nodes[j]))
    complement = list(set(product_list)-set(edges))
    new_G = nx.Graph()
    for item in complement:
        new_G.add_edge(item[0],item[1])
    if len(G.nodes)==len(new_G.nodes):
        if nx.is_connected(new_G):
            return new_G
    return None

#   Calculate the L_r of a graph(average distance of a random graph with given m and n)
def lr(G):
    n = len(G.nodes)
    k = 2*len(G.edges)/n
    return log(n)/log(k)