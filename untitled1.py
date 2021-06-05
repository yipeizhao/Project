from quick_test_graph import quick_test_graph
from Ce import Ce
from small_network_test import small_network_test
import matplotlib.pyplot as plt
from MAg import MAg
result=[]
graphs, df = small_network_test()
for i in range(len(graphs)):
    result.append(MAg(graphs[i],normalisation=False))

plt.scatter(df["Number_of_edges"],result)