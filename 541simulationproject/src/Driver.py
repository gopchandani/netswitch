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
        
        self.param1 = numpy.arange(1.0, 10.0, 1.0)
        self.param2 = numpy.arange(1.0, 10.0, 1.0)
        
        self.num_iterations = num_iterations
        self.env = None
        
        self.avg_wait_times = {}

    def run_iterations(self, param1, param2):
        self.avg_wait_times[(param1, param2)]  = []
        
        for i in range(self.num_iterations):
            random.seed()
            self.env = simpy.Environment()
            self.update = Update(self.env, param1, param2, 100)
            self.env.run(until=10000)
            self.avg_wait_times[(param1, param2)].append(numpy.average(self.update.update_wait_times))
                        
    def run_simulation(self):
        for param1 in self.param1:
            for param2 in self.param2:
                self.run_iterations(param1, param2)
                                        
    def process_output(self):
        print self.avg_wait_times

