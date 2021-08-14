import utilities as ut
import pandas as pd
import matplotlib.pyplot as plt
import Complexity as cx
import numpy as np
load_path = "real_networks/processed/"
index = ["dolphins","pdzbase","GBPT_train",
         "hamsterster","Roget","flight"]
load_path_bus = "real_networks/processed/modified_bus/m_"
index_bus = ["london","paris","berlin","sydney","detroit","beijing"]
dfs = [pd.read_csv(load_path+item+".csv") for item in index]
dfs_bus = [pd.read_csv(load_path_bus+item+".csv") for item in index_bus]
networks = [ut.df_to_network(item) for item in dfs]
networks_bus = [ut.df_to_network(item) for item in dfs_bus]

fig,ax = plt.subplots(6,2,figsize=(10,24))

step_prob = 0.05
prob_list = np.linspace(0,1,int(1/step_prob))
sample_number = 10

for n in range(len(networks)):
    result = []
    for i in range(sample_number):
        single_result=[]
        G1 = networks[n].copy()
        for j in range(int(1/step_prob)):
            G2 = G1.copy()
            G1 = ut.single_link_rewiring(G2, step_prob)
            single_result.append(cx.OdC(G1))
        result.append(single_result)
    avg_result = [0]*int(1/step_prob)
    for i in range(len(prob_list)):
        for j in range(len(result)):
            avg_result[i] = avg_result[i] + result[j][i]
    avg_result = [item/len(result) for item in avg_result]
    ax[n][0].plot(prob_list,avg_result)
    
for n in range(len(networks_bus)):
    result = []
    for i in range(sample_number):
        single_result=[]
        G1 = networks_bus[n].copy()
        for j in range(int(1/step_prob)):
            G2 = G1.copy()
            G1 = ut.single_link_rewiring(G2, step_prob)
            single_result.append(cx.OdC(G1))
        result.append(single_result)
    avg_result = [0]*int(1/step_prob)
    for i in range(len(prob_list)):
        for j in range(len(result)):
            avg_result[i] = avg_result[i] + result[j][i]
    avg_result = [item/len(result) for item in avg_result]
    ax[n][1].plot(prob_list,avg_result)