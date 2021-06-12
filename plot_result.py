from utilities import small_network_test,small_world_property
import matplotlib.pyplot as plt
import Complexity

#Parameter
normalisation = True
n = 50
use_all_m = False
sample = 300

result=[]
graphs, df = small_network_test(n,use_all_m,sample)
df = small_world_property(df)
small_worlds_edge = []
small_worlds_result = []
for i in range(len(graphs)):
   result.append(Complexity.Cr(graphs[i],normalisation=normalisation))
   if df["Small_world"][i]== 1:
       small_worlds_edge.append(df["Number_of_edges"][i])
       small_worlds_result.append(result[i])
plt.scatter(df["Number_of_edges"],result,marker = 'x',label = "Normal")
plt.scatter(small_worlds_edge,small_worlds_result,marker = 'o',color = 'red',label = "Small world")
plt.title("n="+str(n))
plt.legend()