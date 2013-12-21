'''
Created on Dec 18, 2013

@author: rakesh
'''

class Update(object):
    '''
    classdocs
    '''


    def __init__(self, creation_time):
        '''
        Constructor
        '''
        
        
        #When was the update created
        self.creation_time = creation_time
        
        #When did update arrive at a given hop?
        self.hop_arrival_times = []
        
        #How long did the update wait on a given hop?
        self.hop_wait_times = []
        
        #How lonng did it take to process the update on a given hop?
        self.hop_processing_times = []
        
            
    def total_waiting_time(self):
        return sum(self.hop_wait_times)
    
    def total_processing_time(self):
        return sum(self.hop_processing_times)

    
    