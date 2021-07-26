import utilities as ut
import Complexity as cx
import matplotlib.pyplot as plt

normalisation = True
n = 20
use_all_m = False
sample = 1000
method1 = "Cr"
measure_method1 = getattr(cx,method1)
method2 = "Ce"
measure_method2 = getattr(cx,method2)
result1=[];result2=[]
graphs, df = ut.random_networks(n,use_all_m,sample)

for i in range(len(graphs)):
   result1.append(measure_method1(graphs[i],normalisation=normalisation))
   result2.append(measure_method2(graphs[i],normalisation=normalisation))
df = df.sort_index()
plt.scatter(result1,result2,c = df["Number_of_edges"])
plt.xlabel(method1)
plt.ylabel(method2)
plt.title("n=" + str(n))
plt.colorbar()