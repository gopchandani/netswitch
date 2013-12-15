'''
Created on Dec 10, 2013

@author: rakesh
'''

import logging
import simpy
import numpy
import random
from Update import Update

class Driver(object):
    def __init__ (self, num_iterations):
        
        self.num_iterations = num_iterations
        self.env = None
        self.avg_wait_times = []


    def run_simulation(self):
        
        for i in range(self.num_iterations):
            random.seed()
            self.env = simpy.Environment()
            self.update = Update(self.env, 1.0, 0.1, 100)
            self.env.run(until=10000)
            self.avg_wait_times.append(numpy.average(self.update.update_wait_times))
            
    def process_output(self):
        print self.avg_wait_times

