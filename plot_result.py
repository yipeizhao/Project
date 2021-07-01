from utilities import random_networks,small_world_property,BA_random_graphs,WS_random_graphs,NW_random_graphs
import matplotlib.pyplot as plt
import Complexity

#Parameter
normalisation = True
n = 20
use_all_m = False
sample = 750
method1 = "Ce"
measure_method1 = getattr(Complexity,method1)
# method2 = "OdC"
# measure_method2 = getattr(Complexity,method2)

result1=[];result2=[]
graphs, df = random_networks(n,use_all_m,sample)
small_worlds_edge = []
small_worlds_result = []
power_law_edge=[]
power_law_result = []

for i in range(len(graphs)):
   result1.append(measure_method1(graphs[i],normalisation=normalisation))
#    if df["Small_world"][i]== 1:
#        small_worlds_edge.append(df["Number_of_edges"][i])
#        small_worlds_result.append(result1[i])

   if df["Power_law"][i] == 1:
       power_law_edge.append(df["Number_of_edges"][i])
       power_law_result.append(result1[i])

# # for i in range(len(graphs)):
#     result2.append(measure_method2(graphs[i],normalisation=normalisation))

df = df.sort_index()
df["Complexity"] = result1
plt.scatter(df["Number_of_edges"],result1,marker = 'x',color = 'black',alpha = 0.7,label = "Random graphs")

# plt.scatter(small_worlds_edge,small_worlds_result,marker = 'o',color = 'red',label = "Small world")
plt.scatter(power_law_edge,power_law_result,color = 'blue',label = "Power law")

# BA_graphs = BA_random_graphs(n,int(len(graphs)/5))
# BA_edges = []
# BA_result = []
# for i in range(int(len(graphs)/5)):
#     BA_edges.append(len(BA_graphs[i].edges))
#     BA_result.append(measure_method(BA_graphs[i]))
# plt.scatter(BA_edges,BA_result,marker = 'o',color = 'pink',label='BA graphs')

# WS_graphs = WS_random_graphs(n,int(len(graphs)/5))
# WS_edges = []
# WS_result = []
# for i in range(int(len(graphs)/5)):
#     WS_edges.append(len(WS_graphs[i].edges))
#     WS_result.append(measure_method(WS_graphs[i]))
# plt.scatter(WS_edges,WS_result,marker = 'o',color = 'green',label='WS graphs')


# NW_graphs = NW_random_graphs(n,int(len(graphs)/5))
# NW_edges = []
# NW_result = []
# for i in range(int(len(graphs)/5)):
#     NW_edges.append(len(NW_graphs[i].edges))
#     NW_result.append(measure_method(NW_graphs[i]))
# plt.scatter(NW_edges,NW_result,marker = 'o',color = 'orange',label='NW graphs')

plt.title(method1+" " + "n="+str(n))
plt.legend()

plt.figure()
# plt.scatter(result1,result2)
# plt.xlabel(method1);plt.ylabel(method2)
