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
                
    #Calculating a_k
    a_k=[]
    for i in range(max_degree):
        a_k.append(sum(degree_correlation[i]))
    A = sum(a_k)
    if A !=0:
        for i in range(len(a_k)):
            a_k[i]=a_k[i]/A
    
    #Calculating the complexity
    complexity = 0
    for item in a_k:
        complexity -= item*ln(item)
    
    #Normalisation
    if normalisation == True:
        complexity = complexity/(ln(len(G.degree)-1))
    return complexity


def ln(x):
    if x == 0:
        return 0
    else:
        return np.log(x)