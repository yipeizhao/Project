import utilities

def C1est(G,normalisation = True):
    n = len(G.nodes)
    mcu = n**1.68-10
    N1est = len(utilities.isomorphic_graphs(G))
    if normalisation == False:
        return N1est
    else:
        return (N1est-1)/(mcu-1)