import networkx as nx
import pandas as pd
import numpy as np

def small_world_property(df):
    df_list = []
    if len(df)>400:
        df=df.sort_values(by=['Number_of_edges'])
        for i in range(0,len(df),5):
            df_list.append(df[i:i+5])
        
        for dfs in df_list:
            small_world_parameter = []
            avg_distance = np.mean(dfs['Average_distance'])
            avg_clustering = np.mean(dfs['Average_clustering'])
            for index,rows in dfs.iterrows():
                small_world_parameter.append((rows['Average_clustering']*avg_distance)/(rows['Average_distance']*avg_clustering))
            for i in range(len(small_world_parameter)):
                if small_world_parameter[i]>1:
                    dfs.iloc[i]['Small_world']=1
                    
            
            
    return pd.concat(df_list)
