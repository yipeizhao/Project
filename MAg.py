from math import log10
def MAg(G):
    degree_view = list(G.degree)
    degree_list =[node[1] for node in degree_view]
    n = len(degree_list)
    m = len(G.edges)
    R = 0
    I = 0
    for i in range(n):
        for j in range(i+1,n):
            R = R + log10(degree_list[i]*degree_list[j])
            I = I + log10((2*m)/(degree_list[i]*degree_list[j]))
    R = R / m
    I = I / m
    R_c = 2*log10(n-1)
    R_p = 2*((n-2)/(n-1))*log10(2)
    I_c = log10(n/(n-1))
    I_p = log10(n-1)-((n-3)/(n-1))*log10(2)
    MA_R = 4*((R-R_p)/(R_c-R_p))*(1-(R-R_p)/(R_c-R_p))
    MA_I = 4*((I-I_p)/(I_p-I_c))*(1-(I-I_p)/(I_p-I_c))
        
        
    return MA_R*MA_I