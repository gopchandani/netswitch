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
        self.update_processor = env.process(self.update_processing())

        self.updates_processed = 0
        self.total_update_wait_time = 0.0
        self.total_update_processing_time = 0.0
                
        self.processing_pipe = simpy.Store(self.env) 
        self.aggregator_link = None

         
    def update_processing(self):        
        while True:
            
            update = yield self.processing_pipe.get()
            
            update_arrival_time = self.env.now
            update.hop_arrival_times.append(update_arrival_time)
            
            self.updates_processed = self.updates_processed + 1
            
            #Only process if the update was created before right now.
            if self.env.now >= update.creation_time:
                
                #Store the time the update waited for before it was processed
                curr_wait_time = self.env.now - update_arrival_time
                update.hop_wait_times.append(curr_wait_time)

                self.total_update_wait_time += curr_wait_time
                
                #Yield for amount of time it takes to process locally
                yield self.env.timeout(random.expovariate(self.update_service_rate))
                                
                #Store the total
                curr_proessing_time = self.env.now - update_arrival_time
                update.hop_processing_times.append(curr_proessing_time)
                
                self.total_update_processing_time += curr_proessing_time
                
                
                
                if self.aggregator_link != None:
                    
                    #Decide if this update needs remote processing
                    send_to_aggregator = random.randint(0,1)  
                    if send_to_aggregator == 1:
                        
                        #If it does, put it on the appropriate link
                        self.aggregator_link.put(update)
                
                