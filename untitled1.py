from quick_test_graph import quick_test_graph
from Ce import Ce
from small_network_test import small_network_test
import matplotlib.pyplot as plt
from MAg import MAg
from OdC import OdC
from Cr import Cr
#Parameter
normalisation = True
n = 7
use_all_m = True
sample = 50
result=[]


graphs, df = small_network_test(n,use_all_m,sample)

small_worlds_edge = []
small_worlds_result = []
for i in range(len(graphs)):
   result.append(Ce(graphs[i],normalisation=normalisation))
   if df["Small_world"][i]== 1:
       small_worlds_edge.append(df["Number_of_edges"][i])
       small_worlds_result.append(result[i])
plt.scatter(df["Number_of_edges"],result,marker = 'x',label = "Normal")
plt.scatter(small_worlds_edge,small_worlds_result,marker = 'o',color = 'red',label = "Small world")
plt.title("n="+str(n))
plt.legend()