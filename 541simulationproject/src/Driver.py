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
from Update import Update

class Driver(object):
    def __init__ (self, num_iterations, time_until):
        
        self.param1 = np.arange(0.01, 2.0, 0.1)
        self.param2 = [1.0]#np.arange(0.1, 2.0, 0.2)
        self.current_param = ()
        
        self.num_iterations = num_iterations
        self.time_until = time_until
        
        self.env = None

        self.avg_processing_times = {}        
        self.avg_wait_times = {}
        
        self.updates = []
        
    def prepare_topology(self):

        #Build controllers        
        self.controller1 = Controller(self.env, self.current_param[0], self.current_param[1])
        self.controller2 = Controller(self.env, self.current_param[0], self.current_param[1])
        
        #Build an aggregator 
        self.aggregator = Controller(self.env, self.current_param[0], self.current_param[1])
        
        #Put a link between the two        
        self.controller1.aggregator_link = self.aggregator.processing_pipe
        self.controller2.aggregator_link = self.aggregator.processing_pipe
        
    
    def update_generator(self):
        while True:
            
            #Wait for a random amount of time before generating the next update
            yield self.env.timeout(random.expovariate(self.current_param[0]))
                        
            #Put things on the local pipe
            update = Update(self.env)            
            update.hop(self.controller1.processing_pipe)
            self.updates.append(update)

            update = Update(self.env)            
            update.hop(self.controller2.processing_pipe)
            self.updates.append(update)
                        
                        
    def setup_environment(self):
        
        random.seed()
        
        self.updates = []
        
        self.env = simpy.Environment()
        self.prepare_topology()
        
        update_generator = self.env.process(self.update_generator())
            
    def run_iterations(self):

        for i in range(self.num_iterations):
            self.setup_environment()
            self.env.run(until = self.time_until)
            self.stats_collect() 
        
    def stats_init(self):
        
        self.avg_wait_times[self.current_param]  = {}
        self.avg_wait_times[self.current_param]['iterations_output'] = []
 
        self.avg_processing_times[self.current_param]  = {}
        self.avg_processing_times[self.current_param]['iterations_output'] = []
    
    def stats_collect(self):
        total_updates_processed = 0
        total_update_wait_time = 0
        total_update_processing_time = 0
        
        for u in self.updates:
            if u.has_been_processed == True:
                total_updates_processed += 1
                total_update_wait_time += u.total_waiting_time()
                total_update_processing_time += u.total_processing_time()
                
        avg_wait_time = total_update_wait_time / total_updates_processed
        self.avg_wait_times[self.current_param]['iterations_output'].append(avg_wait_time)

        avg_processing_time = total_update_processing_time / total_updates_processed
        self.avg_processing_times[self.current_param]['iterations_output'].append(avg_processing_time)


    def stats_aggregate(self):
 
        self.avg_wait_times[self.current_param]['average'] = np.average(self.avg_wait_times[self.current_param]['iterations_output'])
        self.avg_wait_times[self.current_param]['sd'] = np.std(self.avg_wait_times[self.current_param]['iterations_output'])

        self.avg_processing_times[self.current_param]['average'] = np.average(self.avg_processing_times[self.current_param]['iterations_output'])
        self.avg_processing_times[self.current_param]['sd'] = np.std(self.avg_processing_times[self.current_param]['iterations_output'])
        
        print 'Average Wait Time:', self.avg_wait_times[self.current_param]['average']
        print 'SD Processing Time:', self.avg_processing_times[self.current_param]['sd']
        print 'Average Wait Time:', self.avg_wait_times[self.current_param]['average']
        print 'SD Processing Time:', self.avg_processing_times[self.current_param]['sd']

                
    def run_simulation(self):
        
        
        #Loop over possible values of parameters
        for param1 in self.param1:
            for param2 in self.param2:
                self.current_param = (param1, param2)
                self.stats_init()
                
                print '--- Param1:', self.current_param[0], 'Param2:', self.current_param[1]
                
                self.run_iterations()
                
                self.stats_aggregate()
    
    
    def display_graph_of_wait_times_with_changing_arrival_rate(self):
        plt.figure()
        
        data_df = np.repeat(self.num_iterations, len(self.param1))

        avg_wait_times = []
        sd_wait_times = []
        
        for arrival_rate in self.param1:
            current_param = (arrival_rate, self.param2)
            avg_wait_times.append(self.avg_wait_times[current_param]['average'])
            sd_wait_times.append(self.avg_wait_times[current_param]['sd'])
        
        data_m = np.array(avg_wait_times)
        data_sd = np.array(sd_wait_times)   

        plt.errorbar(self.param1, data_m, yerr=ss.t.ppf(0.95, data_df)*data_sd)
        
        plt.xlim((-1,4))
        plt.show()    
    
    
    
    
    
    
    
    
    
    
    
    
    
#    
#    def prepare_goods_for_graph(self):                     
#        
#        for param_tuple in self.avg_wait_times.keys():
#            print param_tuple, self.avg_wait_times[param_tuple]['iterations_output']
#
#            self.avg_wait_times[param_tuple]['data_point'] = np.average(self.avg_wait_times[param_tuple]['iterations_output'])                        
#            self.avg_wait_times[param_tuple]['data_sd'] = np.std(self.avg_wait_times[param_tuple]['iterations_output'])
#            self.avg_wait_times[param_tuple]['yerr'] = ss.t.ppf(0.95, self.num_iterations - 1)*self.avg_wait_times[param_tuple]['data_sd']
#    
#    def display_graphs(self):
#        plt.figure()
#        data_m=np.array([1,2,3,4])
#        data_df=np.array([5,6,7,8])
#        
#        data_sd=np.array([11,12,12,14])   
#
#        plt.errorbar([0,1,2,3], data_m, yerr=ss.t.ppf(0.95, data_df)*data_sd)
#        
#        plt.xlim((-1,4))
#        plt.show()
#                
#    def process_output(self):
#        
#        self.prepare_goods_for_graph()
#        self.display_graphs()
