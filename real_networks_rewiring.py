import utilities as ut
import pandas as pd
import matplotlib.pyplot as plt
import Complexity as cx
import numpy as np
load_path = "real_networks/processed/"
index = ["bitcoin","coauthorship","GBPT_train",
         "hamsterster","Roget","flight"]
load_path_bus = "real_networks/processed/modified_bus/m_"
index_bus = ["london","paris","berlin","sydney","detroit","beijing"]
dfs = [pd.read_csv(load_path+item+".csv") for item in index]
dfs_bus = [pd.read_csv(load_path_bus+item+".csv") for item in index_bus]
networks = [ut.df_to_network(item) for item in dfs]
networks_bus = [ut.df_to_network(item) for item in dfs_bus]

fig,ax = plt.subplots(6,2,figsize=(10,24))


prob_list = np.linspace(0.3,0.7,5)
for i in range(len(networks)):
    result_1 = [cx.OdC(ut.single_link_rewiring(networks[i],prob)) for prob in prob_list]
    result_2 = [cx.OdC(ut.single_link_rewiring(networks_bus[i],prob)) for prob in prob_list]
    ax[i][0].plot(prob_list,result_1)
    ax[i][1].plot(prob_list,result_2)