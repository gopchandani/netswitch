'''
Created on Dec 15, 2013

@author: rakesh
'''
import random
import simpy


class Controller(object):
    '''
    classdocs
    '''
    
    def __init__(self, env, update_arrival_rate, update_service_rate):#, destination_pipes):
        '''
        Constructor
        '''
        self.update_arrival_rate = update_arrival_rate 
        self.update_service_rate = update_service_rate 

        self.env = env
        self.local_generation_processor = env.process(self.local_update_generation())
        self.local_processing_processor = env.process(self.local_update_processing())

        self.updates_created = 0
        self.updates_processed = 0
        self.total_update_wait_time = 0.0
        self.total_update_processing_time = 0.0
                
        self.local_pipe = simpy.Store(self.env)
 
    
    def local_update_generation(self):
        while True:
            
            #Wait for a random amount of time before generating the next update
            yield self.env.timeout(random.expovariate(self.update_arrival_rate))
                        
            #Put things on the local pipe
            update = {}
            update['creation_time'] = self.env.now
            self.local_pipe.put(update)
            
            #Update stats
            self.updates_created = self.updates_created + 1
            
                
    def local_update_processing(self):        
        while True:
            
            update = yield self.local_pipe.get()
            self.updates_processed = self.updates_processed + 1
            
            #Only process if the update was created before right now.
            if self.env.now >= update['creation_time']:
                
                #Store the time the update waited for before it was processed
                update['wait_time'] = self.env.now - update['creation_time']
                self.total_update_wait_time += update['wait_time']
                
                #Yield for amount of time it takes to process locally
                yield self.env.timeout(random.expovariate(self.update_service_rate))
                                
                #Store the total
                update['processing_time'] = self.env.now - update['creation_time']
                self.total_update_processing_time += update['processing_time']
                
            else:
                print('here 2')