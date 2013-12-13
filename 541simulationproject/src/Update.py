'''
Created on Dec 10, 2013

@author: rakesh
'''

import logging
import random
import simpy


class Update(object):
    '''
    This class contains methods for simulation Rule Updates.
    '''

    def __init__(self, env, per_hop_service_rate, num_updates, update_arrival_rate):
        '''
        Constructor
        '''
        self.env = env
        self.proc = env.process(self.update_generation())
        self.per_hop_service_rate = per_hop_service_rate
        self.num_updates = num_updates
        self.arrival_rate = update_arrival_rate
        
        self.aggregator_hops_affected = None
        self.service_rate = None
        
        
        #Define the resources that updates are going to use:
        #TODO: Allow for multiple hops to be.
        self.aggregator = simpy.Resource(self.env, capacity=1)
        
    def update_generation(self):
        for i in range(self.num_updates):
            
            #Wait for a random amount of time before generating the next update
            yield self.env.timeout(random.expovariate(self.arrival_rate))
            
    '''
    This class contains methods for simulation Rule Updates.
    '''

    def __init__(self, env, per_hop_service_rate, num_updates, update_arrival_rate):
        '''
        Constructor
        '''
        self.env = env
        self.proc = env.process(self.update_generation())
        self.per_hop_service_rate = per_hop_service_rate
        self.num_updates = num_updates
        self.arrival_rate = update_arrival_rate
        
        self.aggregator_hops_affected = None
        self.service_rate = None
        
        
        #Define the resources that updates are going to use:
        #TODO: Allow for multiple hops to be.
        self.aggregator = simpy.Resource(self.env, capacity=1)
        
    def update_generation(self):
        for i in range(self.num_updates):
            
            #Wait for a random amount of time before generating the next update
            yield self.env.timeout(random.expovariate(self.arrival_rate))
            
            #Process the update
            self.env.process(self.update_processing())
                        
        
    def update_processing(self):
    
        #Flip a coin on as to how far the ripple effects of this update will go.        
        #TODO: Make this randomself.aggregator_hops_affected = random.uniform(0, 10)
        self.aggregator_hops_affected = 1.0

        
        #Generate service_rate
        self.service_rate = self.aggregator_hops_affected * self.per_hop_service_rate
        
       
        with self.aggregator.request() as req:
            
            logging.info('%7.4f: Waiting' % (self.env.now))
            
            #Wait for the aggregator to become available
            yield req
            
            start = self.env.now
            logging.info('%7.4f: Starting Processing' % start)
            
            #Yield that amount of time
            yield self.env.timeout(random.expovariate(self.service_rate))
            
            end = self.env.now
            logging.info('%7.4f: Ending Processing' % end)            
            
            logging.info('Took: %7.4f' % (end - start))
            
        
        