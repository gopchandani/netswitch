'''
Created on Dec 10, 2013

@author: rakesh
'''

import random
import simpy

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

from Update import Update

class Driver(object):
    def __init__ (self, num_iterations):
        
        self.param1 = [1.0]#np.arange(1.0, 10.0, 1.0)
        self.param2 = np.arange(0.1, 2.0, 0.2)
        
        self.num_iterations = num_iterations
        self.env = None
        
        self.avg_wait_times = {}


    def run_iterations(self, param1, param2):
        self.avg_wait_times[(param1, param2)]  = {}
        self.avg_wait_times[(param1, param2)]['iterations_output'] = []
        
        for i in range(self.num_iterations):
            random.seed()
            self.env = simpy.Environment()
            
            #Flip a coin on as to how far the ripple effects of this update will go.        
            #TODO: Make this randomself.aggregator_hops_affected = random.uniform(0, 10)
            #TODO: Allow for multiple hops to be.
            
            aggregators = [simpy.Resource(self.env, capacity=1)]
            
            self.update = Update(self.env, param1, param2, 1.0, aggregators, 10)
            self.env.run(until=10000)
            self.avg_wait_times[(param1, param2)]['iterations_output'].append(np.average(self.update.update_wait_times))
        
        self.avg_wait_times[(param1, param2)]['average'] = np.average(self.avg_wait_times[(param1, param2)]['iterations_output'])
        print 'Param1:', param1, 'Param2:', param2, 'Average Wait Time:', self.avg_wait_times[(param1, param2)]['average']
        
    def run_simulation(self):
        for param1 in self.param1:
            for param2 in self.param2:
                self.run_iterations(param1, param2)
                             
    
    def prepare_goods_for_graph(self):                     
        
        for param_tuple in self.avg_wait_times.keys():
            print param_tuple, self.avg_wait_times[param_tuple]['iterations_output']

            self.avg_wait_times[param_tuple]['data_point'] = np.average(self.avg_wait_times[param_tuple]['iterations_output'])                        
            self.avg_wait_times[param_tuple]['data_sd'] = np.std(self.avg_wait_times[param_tuple]['iterations_output'])
            self.avg_wait_times[param_tuple]['yerr'] = ss.t.ppf(0.95, self.num_iterations - 1)*self.avg_wait_times[param_tuple]['data_sd']
    
    def display_graphs(self):
        plt.figure()
        data_m=np.array([1,2,3,4])
        data_df=np.array([5,6,7,8])
        
        data_sd=np.array([11,12,12,14])   

        plt.errorbar([0,1,2,3], data_m, yerr=ss.t.ppf(0.95, data_df)*data_sd)
        
        plt.xlim((-1,4))
        plt.show()
                
    def process_output(self):
        
        self.prepare_goods_for_graph()
        self.display_graphs()
