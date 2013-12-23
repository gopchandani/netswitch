'''
Created on Dec 10, 2013

@author: rakesh
'''

import inspect
import random
import simpy

import math
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

from Controller import Controller
from Update import Update

class Driver(object):
    def __init__ (self, num_iterations, time_until, num_aggregator_levels, num_controllers_per_aggregators, arrival_rate_range, service_rate_range, hop_probs):
        
        self.aggregators = []
        self.controllers = []
        
        self.num_aggregator_levels = num_aggregator_levels
        self.num_controllers_per_aggregators = num_controllers_per_aggregators
        
        self.param1 = arrival_rate_range
        self.param2 = service_rate_range
        self.param3 = hop_probs
        self.param4 = num_aggregator_levels
        
        self.current_param = ()
        
        self.num_iterations = num_iterations
        self.time_until = time_until
        
        self.env = None

        self.avg_processing_times = {}        
        self.avg_wait_times = {}
        
        self.updates = []
        
    def prepare_topology(self):

        self.updates = []
        self.aggregators = []
        self.controllers = []
                
        higher_level_aggs = []

        #Build the controller-aggregator tree from top-down
        for l in range(self.current_param[3]):
                                    
            #Is it the top-level of hierarchy?
            if l == 0:
                #Just create a single aggregator.
                aggregator = Controller(self.env, self.current_param[1], [])
                higher_level_aggs.append(aggregator)
            
            #In the middle layers, aggregators aggregate
            else:
                new_higher_level_aggs = []
                
                #For each higher-layer aggregator, create num_controllers_per_aggregators aggregators
                for hla in higher_level_aggs:
                    for a in range(self.num_controllers_per_aggregators):        
                        hla_list = [hla] + hla.hla_list
                        aggregator = Controller(self.env,  self.current_param[1], hla_list)
                        new_higher_level_aggs.append(aggregator)
                
                higher_level_aggs = new_higher_level_aggs
            
        # if it is bottom level, build controllers
        for hla in higher_level_aggs:   
            for c in range(self.num_controllers_per_aggregators):
                hla_list = [hla] + hla.hla_list
                
                controller = Controller(self.env, self.current_param[1], hla_list)
                
                #Keep track of all controllers to feed them updates
                self.controllers.append(controller)        

        
    def update_generator(self):
        while True:
            
            #Wait for a random amount of time before generating the next update
            #Scale the rate s.t. each controller roughly gets to see lambda rate by means of splitting
            
            yield self.env.timeout(random.expovariate(len(self.controllers) * self.current_param[0]))
            
            #Select a uniformly random controller from all the ones that have been generated            
            controller = random.choice(self.controllers)

            #Create an update and hop it on
            update = Update(self.env, controller, controller.hla_list, self.current_param[2])            
            
            self.updates.append(update)
                        
            self.env.process(update.process_update())
                        
    def setup_environment(self):
        
        random.seed()
                
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
         
        
        if total_updates_processed > 0: 
                
            avg_wait_time = total_update_wait_time / total_updates_processed
            self.avg_wait_times[self.current_param]['iterations_output'].append(avg_wait_time)
    
            avg_processing_time = total_update_processing_time / total_updates_processed
            self.avg_processing_times[self.current_param]['iterations_output'].append(avg_processing_time)

    def compute_se(self, listnum, mean):
        square_sum = 0.0

        for num in listnum:
            square_sum = pow(num - mean, 2)
        
        se = math.sqrt((1.0/(len(listnum) - 1)) * square_sum)
        return se
        

    def stats_aggregate(self):
        
        self.avg_wait_times[self.current_param]['average'] = np.average(self.avg_wait_times[self.current_param]['iterations_output'])
        self.avg_wait_times[self.current_param]['sd'] = np.std(self.avg_wait_times[self.current_param]['iterations_output'])
        self.avg_wait_times[self.current_param]['se'] = self.compute_se(self.avg_wait_times[self.current_param]['iterations_output'], self.avg_wait_times[self.current_param]['average'])
        self.avg_wait_times[self.current_param]['df'] = len(self.avg_wait_times[self.current_param]['iterations_output'])


        self.avg_processing_times[self.current_param]['average'] = np.average(self.avg_processing_times[self.current_param]['iterations_output'])
        self.avg_processing_times[self.current_param]['sd'] = np.std(self.avg_processing_times[self.current_param]['iterations_output'])
        self.avg_processing_times[self.current_param]['se'] = self.compute_se(self.avg_processing_times[self.current_param]['iterations_output'], self.avg_processing_times[self.current_param]['average'])
        self.avg_processing_times[self.current_param]['df'] = len(self.avg_processing_times[self.current_param]['iterations_output'])

        print 'Total Processed Updates:', self.avg_processing_times[self.current_param]['df']
        print 'Average Processing Time:', self.avg_processing_times[self.current_param]['average']
        print 'SE Processing Time:', self.avg_processing_times[self.current_param]['se']


    def stats_analyze(self):

        self.avg_processing_times[self.current_param]['average'] = np.average(self.avg_processing_times[self.current_param]['iterations_output'])
        self.avg_processing_times[self.current_param]['sd'] = np.std(self.avg_processing_times[self.current_param]['iterations_output'])
        self.avg_processing_times[self.current_param]['se'] = self.compute_se(self.avg_processing_times[self.current_param]['iterations_output'], self.avg_processing_times[self.current_param]['average'])
        self.avg_processing_times[self.current_param]['df'] = len(self.avg_processing_times[self.current_param]['iterations_output'])

        print 'Total Processed Updates:', self.avg_processing_times[self.current_param]['df']
        print 'Average Processing Time:', self.avg_processing_times[self.current_param]['average']
        print 'SE Processing Time:', self.avg_processing_times[self.current_param]['se']

                
    def run_simulation(self):
                
        #Loop over possible values of parameters
        for param1 in self.param1:
            for param2 in self.param2:
                self.current_param = (param1, param2)
                
                print self.current_param
                
                self.stats_init()
                                
                self.run_iterations()
                self.stats_aggregate()
    
    def run_2_k_study(self):
        for param1 in [self.param1[0], self.param1[len(self.param1) - 1]]:
            for param2 in [self.param2[0], self.param2[len(self.param2) - 1]]:
                for param3 in [self.param3[0], self.param3[len(self.param3) - 1]]:
                    for param4 in [self.param4[0], self.param4[len(self.param4) - 1]]:
                        self.current_param = (param1, param2, param3, param4)
                        print self.current_param
                        self.stats_init()
                        self.run_iterations()
                        self.stats_aggregate()

        for param in self.avg_processing_times.keys():
            print param
            print self.avg_processing_times[param]
    
    def graph_process_times_with_changing_arrival_rate(self):
        plt.figure()
        

        avg_processing_times = []
        se_processing_times = []
        num_processing_times = []
        
        for arrival_rate in self.param1:
            current_param = (arrival_rate, self.param2[0])
            avg_processing_times.append(self.avg_processing_times[current_param]['average'])
            se_processing_times.append(self.avg_processing_times[current_param]['se'])
            num_processing_times.append(self.avg_processing_times[current_param]['df'])
            
        data_m = np.array(avg_processing_times)
        data_se = np.array(se_processing_times)   

        plt.errorbar(self.param1, data_m, yerr=ss.t.ppf(0.95, num_processing_times)*data_se)
        
        plt.xlim((min(self.param1) -1, max(self.param1) + 1))
        plt.xlabel('Arrival Rate (Updates/ms)')
        plt.ylabel('Avg. Update Processing Time (ms)')
        #plt.show()    
        plt.savefig('graph_process_times_with_changing_arrival_rate_num_aggs_' + str(self.current_param[3]) + '_num_ctrls_per_aggs_' + str(self.num_controllers_per_aggregators))
    
    
    