import networkx as nx
import numpy as np
def OdC(G,normalisation = True):
    #Create a degree correlation matrix, using the max degree 
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    max_degree = max(degree_sequence)
    degree_correlation = np.zeros((max_degree,max_degree))
    
    #Building the correlation matrix
    for node in list(G.nodes):
        #An array to store all the neighbors degrees
        neighbors_degree = []
        #Getting the degree of the current node
        node_degree = G.degree(node)
        #Stating all neighbors and finding their degrees
        neighbors = list(G.neighbors(node))
        neighbors_degrees_tuple=G.degree(neighbors)
        for item in neighbors_degrees_tuple:
            neighbors_degree.append(item[1])
        #For every occurence, adding one to the matrix
        for item in neighbors_degree:
            if node_degree<=item:
                degree_correlation[node_degree-1,item-1] +=1
                
    #Calculating the sum of each row
    row_sum=[]
    for i in range(max_degree):
        row_sum.append(sum(degree_correlation[i]))
    #Calculating a_k
    for i in range(max_degree):
        if row_sum[i] != 0:
            for j in range(max_degree):
                degree_correlation[i][j]=degree_correlation[i][j]/row_sum[i]
    
    #Calculating entropy
    complexity = 0
    for i in range(max_degree):
        for j in range(max_degree):
            complexity -=degree_correlation[i][j]*ln(degree_correlation[i][j])
            
        
    #Normalisation
    if normalisation == True:
        complexity = complexity/(ln(len(G.degree)-1))
    return complexity


def ln(x):
    if x == 0:
        return 0
    else:
        return np.log(x)