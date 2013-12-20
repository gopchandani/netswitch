'''
Created on Dec 19, 2013

@author: rakesh
'''
import random
import simpy


class Controller(object):
    '''
    classdocs
    '''
    
    def __init__(self, env, update_arrival_rate, update_service_rate):
        '''
        Constructor
        '''
        self.update_arrival_rate = update_arrival_rate 
        self.update_service_rate = update_service_rate 

        self.env = env
        self.proc = env.process(self.update_generation())
        
        self.local_processing_unit = simpy.Resource(self.env, capacity=1)
        self.current_update_num = 0
        self.update_processing_times = []
        
    
    def update_generation(self):
        while True:
            
            #Wait for a random amount of time before generating the next update
            yield self.env.timeout(random.expovariate(self.update_arrival_rate))

            self.current_update_num = self.current_update_num + 1
                        
            #Process the update
            self.env.process(self.update_processing(self.current_update_num))
                
                
    def update_processing(self, update_number):        
                   
        #Update generated
        start = self.env.now
        
        with self.local_processing_unit.request() as req:
            
            #Wait for local processing to be available
            yield req
            
            #Yield for amount of time it takes to process
            yield self.env.timeout(random.expovariate(self.update_service_rate))
        
        end = self.env.now
        
        self.update_processing_times.append(end - start)

    