#include necessary libraries, and setting up the environment
library("reticulate")
library("igraph")
use_python("/zhaoy/anaconda3")

#function1 return the edges list to build the network in networkx
#function2 return the graph itself for testing in the R environment
configuration_model <- function(series){
  g <- sample_degseq(series, method="vl")
  return(as_edgelist(g))
}
return_graph<- function(series){
  g <- sample_degseq(series, method="vl")
  return(g)
}

#python functions
power_law_generator = source_python("power_law_series.py")
construct_network = source_python("construct_network.py")
cx = source_python("Ce.py")
cx = source_python("OdC.py")

#Building the network in python
n = 1000
gamma = 3
gamma_list = seq(gamma-0.7,gamma+0.9,0.1)
results = list()
graphs = list()
for(i in gamma_list){
  print(i)
  series = power_law_series(n,i)
  if(sum(series)%%2 !=0){
    series[1]=series[1]+1
  }
  edge_list = configuration_model(series)
  g = construct_network(edge_list)
  graphs = append(graphs,g)
  result =   OdC(g)
  results = append(results,result)
}

#Calculating the complexity
#OdC(g)
plot(gamma_list,results)
