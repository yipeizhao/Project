import pandas as pd

df  = pd.read_csv("GBPT/edges.csv")
#Extracting London PT
node_df = pd.read_csv("GBPT/nodes.csv")
#Creating the london df
# london_nodes_df = node_df.loc[node_df["zone"]==490]
# london_nodes = list(london_nodes_df["node"])
# ori_node = [];des_node=[];ori_layer=[];des_layer =[]
# for index,rows in df.iterrows():
#     if rows["ori_node"] in london_nodes:
#         ori_node.append(rows["ori_node"])
#         des_node.append(rows["des_node"])
#         ori_layer.append(rows["ori_layer"])
#         des_layer.append(rows["des_layer"])
        

# london_df = pd.DataFrame({"ori_node":ori_node,
#                           "des_node":des_node,
#                           "ori_layer":ori_layer,
#                           "des_layer":des_layer
#                           })
# london_df.to_csv("GBPT/processed/london_df.csv")

london_df = pd.read_csv("GBPT/processed/london_df.csv")

ori_node = london_df["ori_node"]
des_node = london_df["des_node"]
ori_layer = london_df["ori_layer"]
des_layer = london_df["des_layer"]

rail_ori = []
rail_des = []
for i in range(len(london_df)):
    if ori_layer[i] == 2 and des_layer[i] == 2:
        rail_ori.append(ori_node[i])
        rail_des.append(des_node[i])
data = {    
    "source": rail_ori,
    "target": rail_des
    }
rail_network  = pd.DataFrame(data=data)
rail_network.to_csv("GBPT/processed/GBPT_train.csv",index=False)

bus_ori = []
bus_des = []
for i in range(len(london_df)):
    if ori_layer[i] == 5 and des_layer[i] == 5:
        bus_ori.append(ori_node[i])
        bus_des.append(des_node[i])
data = {    
    "source": bus_ori,
    "target": bus_des
    }
london_bus = pd.DataFrame(data=data)
london_bus.to_csv("GBPT/processed/london_bus.csv",index = False)


