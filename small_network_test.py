import networkx as nx
from random import randint
import pandas as pd

def small_network_test(n=7,use_all_m = True,sample_number = 50):
    #Create a list of list to store all the graphs
    graph_list = []
    #Max number of edges.
    #If sample number>m , we only take m number experiments
    #Sample number>m will cause inefficient creation of graphs.
    m = (n*(n-1))/2
    m = int(m)
    #Create a df to store relevant information
    column_names = ["Number_of_edges","Average_degree","Average_degree_rank",
                    "Average_distance","Average_distance_rank",
                    "Average_clustering","Average_clustering_rank",
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
    
    
    if use_all_m == True:
        count = 0
        for i in range(m+1):
            for j in range(sample_number):
                temp_graph = nx.gnm_random_graph(n,i)
                graph_list.append(temp_graph)
                df["Number_of_edges"][count] = i
                df["Average_degree"][count] =  (2*i)/n
                df["Average_clustering"][count] = nx.average_clustering(temp_graph)
                if nx.is_connected(temp_graph):
                    df["Average_distance"][count] = nx.average_shortest_path_length(temp_graph)
                else:
                    df["Average_distance"][count] = float('nan')
                count+=1

    else:
        for i in range(sample_number):
            edge_number  = randint(0,m)
            temp_graph=nx.gnm_random_graph(n,edge_number)
            graph_list.append(temp_graph)
            df["Number_of_edges"][i] = edge_number
            df["Average_degree"][i] =  (2*edge_number)/n
            df["Average_clustering"][i] = nx.average_clustering(temp_graph)
            if nx.is_connected(temp_graph):
                df["Average_distance"][i] = nx.average_shortest_path_length(temp_graph)
            else:
                df["Average_distance"][i] = float('nan')
                
                
    df["Average_degree_rank"]=ranking(df["Average_degree"])
    df["Average_distance_rank"]=ranking(df["Average_distance"])
    df["Average_clustering_rank"]=ranking(df["Average_clustering"])
    
    #Small wrold property test
    for i in range(len(df)):
        if df["Average_distance_rank"][i]<(len(df)*0.3) and df["Average_clustering_rank"][i]>(len(df)*0.7):
            df["Small_world"][i]=1
    
    return graph_list,df




#Rank all values in a given vector 
#Reference:
#https://codereview.stackexchange.com/questions/65031/creating-a-list-containing-the-rank-of-the-elements-in-the-original-list
def ranking(vector):
    output = [0]*len(vector)
    for i, x in enumerate(sorted(range(len(vector)), key=lambda y: vector[y])):
         output[x] = i
    return output


