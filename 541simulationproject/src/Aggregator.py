'''
Created on Dec 15, 2013

@author: rakesh
'''
from Controller import Controller

class Aggregator():
    '''
    classdocs
    '''


    def __init__(self, env):
        '''
        Constructor
        '''
        self.env = env
        
        self.updates_to_process = 0
        
    #Some kind of loop, always trying to pass things
    def process_updates(self):
        pass
    
    
    
    