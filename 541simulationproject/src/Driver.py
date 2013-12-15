'''
Created on Dec 10, 2013

@author: rakesh
'''

import logging
import simpy
import numpy
from Update import Update

class Driver(object):
    def __init__ (self):
        self.env = simpy.Environment()
        self.update = Update(self.env, 0.1, 1000, 1.0)

    def run_simulation(self):
        self.env.run(until=10000)

    
    def process_output(self):
        print numpy.average(self.update.update_wait_times)

