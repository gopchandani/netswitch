'''
Created on Dec 15, 2013

@author: rakesh
'''
import simpy
import random

from Controller import Controller

class Aggregator():
    '''
    classdocs
    '''


    def __init__(self, env, update_service_rate):
        '''
        Constructor
        '''
        self.env = env        

        self.update_service_rate = update_service_rate   
        self.controller_link = None
        
        self.remote_update_picker_uper = env.process(self.remote_update_pickup())
        self.update_processor = env.process(self.update_processing())
        
        self.updates_created = 0
        self.updates_processed = 0
        self.total_update_wait_time = 0.0
        self.total_update_processing_time = 0.0

        self.processing_pipe = simpy.Store(self.env)
        
        
    def remote_update_pickup(self):
        while True:
            
            #Pick things from the controller links
            update = yield self.controller_link.get()
            
            #Update the timestamp to indicate that this is a different update
            update['hop_creation_time'] = self.env.now
            
            #Put things on the local pipe
            self.processing_pipe.put(update)
            
     
    def update_processing(self):        
        while True:
            
            update = yield self.processing_pipe.get()
            self.updates_processed = self.updates_processed + 1
            
            #Only process if the update was created before right now.
            if self.env.now >= update['hop_creation_time']:
                
                #Store the time the update waited for before it was processed
                curr_wait_time = self.env.now - update['hop_creation_time']
                update['wait_times'].append(curr_wait_time)

                self.total_update_wait_time += curr_wait_time
                
                #Yield for amount of time it takes to process locally
                yield self.env.timeout(random.expovariate(self.update_service_rate))
                                
                #Store the total
                curr_proessing_time = self.env.now - update['hop_creation_time']
                update['processing_times'].append(curr_proessing_time)
                
                self.total_update_processing_time += curr_proessing_time
                

#                #Decide if this update needs remote processing
#                send_to_aggregator = random.randint(0,1)  
#                if send_to_aggregator == 1:
#                    
#                    #If it does, put it on the appropriate link
#                    self.aggregator_link.put(update)
                
                
            else:
                print('here 2')