from utilities import random_networks,small_world_property,BA_random_graphs,WS_random_graphs,NS_random_graphs
import matplotlib.pyplot as plt
import Complexity

#Parameter
normalisation = True
n = 20
use_all_m = False
sample = 300
method = "C1est"
measure_method = getattr(Complexity,method)


result=[]
graphs, df = random_networks(n,use_all_m,sample)
df = small_world_property(df)
# small_worlds_edge = []
# small_worlds_result = []
power_law_edge=[]
power_law_result = []
for i in range(len(graphs)):
   result.append(measure_method(graphs[i],normalisation=normalisation))
   # if df["Small_world"][i]== 1:
   #     small_worlds_edge.append(df["Number_of_edges"][i])
   #     small_worlds_result.append(result[i])
   if df["Power_law"][i] == 1:
       power_law_edge.append(df["Number_of_edges"][i])
       power_law_result.append(result[i])
df = df.sort_index()
df["Complexity"] = result
plt.scatter(df["Number_of_edges"],result,marker = 'x',color = 'black',alpha = 0.7,label = "Normal")
#plt.scatter(small_worlds_edge,small_worlds_result,marker = 'o',color = 'red',label = "Small world")
#plt.scatter(power_law_edge,power_law_result,color = 'blue',label = "Power law")

# BA_graphs = BA_random_graphs(n,sample)
# BA_edges = []
# BA_result = []
# for i in range(int(len(graphs)/5)):
#     BA_edges.append(len(BA_graphs[i].edges))
#     BA_result.append(measure_method(BA_graphs[i]))
# plt.scatter(BA_edges,BA_result,marker = 'o',color = 'red',label='BA graphs')

# WS_graphs = WS_random_graphs(n,sample)
# WS_edges = []
# WS_result = []
# for i in range(int(len(graphs)/5)):
#     WS_edges.append(len(WS_graphs[i].edges))
#     WS_result.append(measure_method(WS_graphs[i]))
# plt.scatter(WS_edges,WS_result,marker = 'o',color = 'green',label='WS graphs')


# NS_graphs = NS_random_graphs(n,sample)
# NS_edges = []
# NS_result = []
# for i in range(int(len(graphs)/5)):
#     NS_edges.append(len(NS_graphs[i].edges))
#     NS_result.append(measure_method(NS_graphs[i]))
# plt.scatter(NS_edges,NS_result,marker = 'o',color = 'orange',label='NS graphs')



plt.title(method+" " + "n="+str(n))
plt.legend()