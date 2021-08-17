import utilities as ut
import Complexity as cx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
class rewiring():
    def __init__(self,name,bus=False,step_prob = 0.05):
        self.name = name
        self.bus = bus
        self.load_network()
        self.step_prob = step_prob
        self.rewired_G = self.G.copy()
        self.result = []
        self.s_n=0
        self.p_n=0
        self.load_result("S")
        self.load_result("P")

    #Load all the networks
    def load_network(self):
        if self.bus == False:
            load_path = "real_networks/processed/"+self.name+".csv"
        else:
            load_path = "real_networks/processed/modified_bus/m_"+self.name+".csv"
        df = pd.read_csv(load_path)
        self.G = ut.df_to_network(df)

    #Carry out one step of single link rewiring
    def single_link_rewiring(self):
        self.rewired_G = ut.single_link_rewiring(self.rewired_G,self.step_prob)
    #Carry out one step of pairwise rewiring
    def pairwise_rewiring(self):
        self.rewired_G = ut.pairwise_rewiring(self.rewired_G,self.step_prob)
    #Reinstantiate the rewired graph
    def clear_rewiring(self):
        self.rewired_G = self.G.copy()
        if cx.OdC(self.rewired_G) != cx.OdC(self.G):
            Exception("Clearing failed")
    #Carry out a sample number of rewiring
    def continuous_rewiring(self,method):
        self.result = [cx.OdC(self.G)]
        if method == "S":
            niter = int(1/self.step_prob)
            for i in range(niter):
                self.single_link_rewiring()
                self.result.append(cx.OdC(self.rewired_G))
            self.s_n += 1
        elif method == "P":
            niter = int(1/self.step_prob)
            for i in range(niter):
                self.pairwise_rewiring()
                self.result.append(cx.OdC(self.rewired_G))
            self.p_n += 1
        else:
            raise ValueError('Insufficient method')
    #Load the calculated result from the data folder
    def load_result(self,method):
        if method =="S":
            try:
                self.s_result = pd.read_csv("result/single_link/"+self.name+".csv")
                self.s_n = len(self.s_result.columns)
            except FileNotFoundError:
                self.s_result = pd.DataFrame(data = {"1":[]})
                self.s_n = 0
        if method =="P":
            try:
                self.p_result = pd.read_csv("result/pairwise/"+self.name+".csv")
                self.p_n = len(self.p_result.columns)
            except FileNotFoundError:
                self.p_result = pd.DataFrame(data = {"1":[]})
                self.p_n = 0
    #Store the result in the class variable result
    def record_result(self,method):
        if method == "S":
            self.s_result[str(self.s_n)] = self.result
        elif method == "P":
            self.p_result[str(self.p_n)] = self.result
        else:
            raise ValueError('Insufficient method')
    #Save the current result table as a csv file
    def write_result(self,method):
        if method == "S" and self.s_n == 0:
            raise Exception("There is no recorded result")
        if method == "P" and self.p_n == 0:
            raise Exception("There is no recorded result")
        if (method == "S+P" or method == "P+S") and (self.s_n == 0 or self.p_n==0):
            raise Exception("There is no recorded result for one/both of the methods.")
        
        if method == "S":
            self.s_result.to_csv("result/single_link/"+self.name+".csv",index = False)
        elif method == "P":
            self.p_result.to_csv("result/pairwise/"+self.name+".csv",index = False)
        elif method == "S+P" or method == "P+S":
            self.s_result.to_csv("result/single_link/"+self.name+".csv",index = False)
            self.p_result.to_csv("result/pairwise/"+self.name+".csv",index = False)
        else:
            raise ValueError('Insufficient method')
    #Carry multiple number of rewiring according to the given parameter
    def experiment(self,method,sample_number):
        if type(sample_number) != type(int(1)):
            ValueError("Insufficient number of samples, please input an integer.")        
        for i in range(sample_number):
            self.clear_rewiring()
            self.continuous_rewiring(method)            
            self.record_result(method)
    #Plot the results
    def plot_result(self,method):
        if method == "S":
            if self.s_n != 0:
                prob_list = np.linspace(0,1,int(1/(self.step_prob)+1))
                mean = [np.mean(row) for index, row in self.s_result.iterrows()]
                std = [0.5*np.std(row) for index, row in self.s_result.iterrows()]
                plt.errorbar(prob_list,mean,yerr = std,color = "black")
            else:
                raise Exception("There is no recorded result")
        elif method == "P":
            if self.p_n != 0:
                prob_list = np.linspace(0,1,int(1/(self.step_prob)+1))
                mean = [np.mean(row) for index, row in self.p_result.iterrows()]
                std = [0.5*np.std(row) for index, row in self.p_result.iterrows()]
                plt.errorbar(prob_list,mean,yerr = std,color = "black")
            else:
                raise Exception("There is no recorded result")
        elif method == "P+S" or method == "S+P":
            if self.s_n !=0 and self.p_n != 0:
                prob_list = np.linspace(0,1,int(1/(self.step_prob)+1))
                mean = [np.mean(row) for index, row in self.s_result.iterrows()]
                std = [0.5*np.std(row) for index, row in self.s_result.iterrows()]
                plt.errorbar(prob_list,mean,yerr = std,color = "black",label = "Single link rewiring")
                
                mean = [np.mean(row) for index, row in self.p_result.iterrows()]
                std = [0.5*np.std(row) for index, row in self.p_result.iterrows()]
                plt.errorbar(prob_list,mean,yerr = std,color = "blue",label = "Pairwise rewiring")
                plt.legend()
                plt.xlabel("Rewiring Probability")
                plt.ylabel("OdC Complexity")
                plt.title("Change of complexity after rewiring")
            else:
                raise Exception("There is no recorded result for one/both of the methods.")
        else:
            raise ValueError('Insufficient method')
    #Carry out a given number of rewiring, saving the result and plotting at the same time.
    def one_stop(self,method,sample_number):
        self.experiment(method,sample_number)
        self.write_result(method)
        self.plot_result(method)