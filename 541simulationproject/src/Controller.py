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
    
    def __init__(self, env, update_service_rate, hla_list):
        '''
        Constructor
        '''
        self.update_service_rate = update_service_rate 
        self.env = env
        self.updates_processed = 0
        self.processing_resource =  simpy.Resource(self.env, capacity = 1)
        self.hla_list = hla_list