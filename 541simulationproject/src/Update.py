'''
Created on Dec 10, 2013

@author: rakesh
'''

import random
import simpy


class Update(object):
    '''
    This class contains methods for simulation Rule Updates.
    '''

    def __init__(self, env, update_arrival_rate, per_hop_service_rate, aggregator_hops_affected, aggregators, num_updates):

        '''
        Constructor
        '''
        self.env = env
        self.proc = env.process(self.update_generation())
        self.update_arrival_rate = update_arrival_rate        
        self.per_hop_service_rate = per_hop_service_rate
        self.aggregator_hops_affected = aggregator_hops_affected
        self.num_updates = num_updates
        
        self.aggregators = aggregators 
        
        #Output vectors
        self.update_wait_times = []
        
    def update_generation(self):
        for i in range(self.num_updates):
            
            #Wait for a random amount of time before generating the next update
            yield self.env.timeout(random.expovariate(self.update_arrival_rate))
            
            #Process the update
            self.env.process(self.update_processing(i))
                        
        
    def update_processing(self, update_num):
        
        #Update just got created. Logs the time of creation
        self.creation_time = self.env.now
        
        #Log the time when you are about to start receiving service
        start = self.env.now
        
        #Go through all the servicer(s)...
        for aggregator in self.aggregators:

            with aggregator.request() as req:

                #Wait for them to be available and provide service
                yield req
                
                #Yield for amount of time it takes to receive service from this guy.
                yield self.env.timeout(random.expovariate(self.per_hop_service_rate))
                
                
        end = self.env.now
                
        self.update_wait_times.append(end - start)
                
                
            
        