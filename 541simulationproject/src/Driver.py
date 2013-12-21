'''
Created on Dec 10, 2013

@author: rakesh
'''

import random
import simpy

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

from Controller import Controller
from Aggregator import Aggregator

class Driver(object):
    def __init__ (self, num_iterations, num_updates_per_iteration):
        
        self.param1 = [1.0]#np.arange(1.0, 10.0, 1.0)
        self.param2 = np.arange(0.1, 2.0, 0.2)
        self.current_param = ()
        
        self.num_iterations = num_iterations
        self.num_updates_per_iteration = num_updates_per_iteration
        
        self.env = None

        self.avg_processing_times = {}        
        self.avg_wait_times = {}
        
    def prepare_topology(self):
        #Flip a coin on as to how far the ripple effects of this update will go.        
        #TODO: Make this randomself.aggregator_hops_affected = random.uniform(0, 10)
        #TODO: Allow for multiple hops to be.

        #Build a switch        
        self.switch = Controller(self.env, self.current_param[0], self.current_param[1])
        
        #Build an aggregator
        self.aggregator = Aggregator(self.env)

        #Put a pipe between the two
        pipe = simpy.Store(self.env)
        
    
    
        
    def setup_environment(self):
        
        random.seed()
        self.env = simpy.Environment()
        self.prepare_topology()
        
            
            
    def run_iterations(self):
        self.avg_wait_times[self.current_param]  = {}
        self.avg_wait_times[self.current_param]['iterations_output'] = []
 
        self.avg_processing_times[self.current_param]  = {}
        self.avg_processing_times[self.current_param]['iterations_output'] = []
        
        for i in range(self.num_iterations):
            self.setup_environment()
            self.env.run(until=1000)

            avg_wait_time = self.switch.total_update_wait_time / self.switch.updates_processed
            self.avg_wait_times[self.current_param]['iterations_output'].append(avg_wait_time)

            avg_processing_time = self.switch.total_update_processing_time / self.switch.updates_processed
            self.avg_processing_times[self.current_param]['iterations_output'].append(avg_processing_time)

        
        self.avg_wait_times[self.current_param]['average'] = np.average(self.avg_wait_times[self.current_param]['iterations_output'])
        print 'Average Wait Time:', self.avg_wait_times[self.current_param]['average']
        
        self.avg_processing_times[self.current_param]['average'] = np.average(self.avg_processing_times[self.current_param]['iterations_output'])
        print 'Average Processing Time:', self.avg_processing_times[self.current_param]['average']
               
                
    def run_simulation(self):
        
        #Loop over possible values of parameters
        for param1 in self.param1:
            for param2 in self.param2:
                self.current_param = (param1, param2)
                print '--- Param1:', self.current_param[0], 'Param2:', self.current_param[1]
                
                self.run_iterations()
    
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
