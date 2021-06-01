import networkx as nx

import pandas as pd

def small_network_test(n=7,sample_number = 50):
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
                    "Average_clustering","Average_clustering_rank"]
    zero_list = [float(0)]*(sample_number*(m+1))
    df = pd.DataFrame(columns = column_names)
    for item in column_names:
        df[item] = zero_list 
        
    #Create graphs and store their information in the df
    count = 0
    for i in range(m+1):
        for j in range(sample_number):
            temp_graph = nx.gnm_random_graph(n,i)
            graph_list.append(temp_graph)
            df["Number_of_edges"][count] = i
            df["Average_degree"][count] =  (2*i)/n
            if nx.is_connected(temp_graph):
                df["Average_distance"][count] = nx.average_shortest_path_length(temp_graph)
            else:
                df["Average_distance"][count] = float('nan')
            df["Average_clustering"][count] = nx.average_clustering(temp_graph)
            count+=1
    df["Average_degree_rank"]=ranking(df["Average_degree"])
    df["Average_distance_rank"]=ranking(df["Average_distance"])
    df["Average_clustering_rank"]=ranking(df["Average_clustering"])
    return graph_list,df

#Rank all values in a given vector 
#Reference:
#https://codereview.stackexchange.com/questions/65031/creating-a-list-containing-the-rank-of-the-elements-in-the-original-list
def ranking(vector):
    output = [0]*len(vector)
    for i, x in enumerate(sorted(range(len(vector)), key=lambda y: vector[y])):
         output[x] = i
    return output


