import utilities as ut
import networkx as nx
from math import log
# G = ut.quick_test_graph()
def STS(G,normalisation = True):
    subs = ut.subgraph_one_edge_deletion(G)
    sensitivity = [ut.number_of_ST(item) for item in subs]
    sensitivity = [item for item in sensitivity if item !=0]
    if len(sensitivity) == 0:
        return 0
    sensitivity = list(sensitivity)
    min_sens = min(sensitivity)
    Sij = [item-min_sens+1 for item in sensitivity]
    a_l = [item/sum(Sij) for item in Sij]
    entropy = 0
    for item in a_l:
        entropy -= item * log(item)
    if normalisation == False:
        return entropy
    else:
        mcu = len(G.nodes)**1.68-10
        normalised_complexity = entropy/log(mcu)
        return normalised_complexity