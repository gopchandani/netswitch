'''
Created on Dec 18, 2013

@author: rakesh
'''

class Update(object):
    '''
    classdocs
    '''


    def __init__(self, env):
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
        
        #How lonng did it take to process the update on a given hop?
        self.hop_processing_times = []
        
            
        
            
    def total_waiting_time(self):
        return sum(self.hop_wait_times)
    
    def total_processing_time(self):
        return sum(self.hop_processing_times)

    def hop(self, link):
        self.current_hop_creation_time = self.env.now
        link.put(self)
    