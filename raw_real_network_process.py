import utilities as ut
import pandas as pd
index = ["bitcoin","coauthorship","GBPT_train",
         "hamsterster","Roget"]
load_file_path = ["real_networks/raw/"+item+".csv" for item in index]
dfs = [pd.read_csv(item) for item in load_file_path]
networks = [ut.df_to_network(g) for g in dfs]
networks = [ut.gcc(g) for g in networks]
processed_df = [ut.network_to_df(g) for g in networks]

save_file_path = ["real_networks/processed/" + item + ".csv" for item in index]
for i in range(len(index)):
    processed_df[i].to_csv(save_file_path[i],index = False)