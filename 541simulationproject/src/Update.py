'''
Created on Dec 18, 2013

@author: rakesh
'''
import simpy
import random

class Update(object):
    '''
    classdocs
    '''


    def __init__(self, env, controller, hla_list):
        '''
        Constructor
        '''
        
        #Environment that the update is from:
        self.env = env
        
        #Has the update been completely processed?
        self.has_been_processed = False
        
        #When was the update created
        self.current_hop_creation_time = self.env.now
        
        #When did update arrive at a given hop?
        self.hop_creation_times = []
        
        #How long did the update wait on a given hop?
        self.hop_wait_times = []
        
        #How long did it take to process the update on a given hop?
        self.hop_processing_times = []
        
        #Which controller was this update produced at?
        self.controller = controller
        
        #Higher level aggregators of the controller where this update was born
        self.hla_list = hla_list
        
            
    def total_waiting_time(self):
        return sum(self.hop_wait_times)
    
    def total_processing_time(self):
        return sum(self.hop_processing_times)

    def process_update(self):
        
        #Do HLA processing
        
        for hla in self.hla_list:
            
            hop_creation_time = self.env.now
            
            with hla.processing_resource.request() as my_turn:
                result = yield my_turn
                
                hop_wait_time = self.env.now - hop_creation_time
                
                #This update has arrived on this aggregator now
                yield self.env.timeout(random.expovariate(hla.update_service_rate))        
                
                
                
                hop_processing_time = self.env.now - hop_creation_time

                self.hop_creation_times.append(hop_creation_time)
                self.hop_wait_times.append(hop_wait_time)
                self.hop_processing_times.append(hop_processing_time)
                
       
        #Do native controller processing
        with self.controller.processing_resource.request() as my_turn:
            result = yield my_turn            
            yield self.env.timeout(random.expovariate(self.controller.update_service_rate))
            self.has_been_processed = True