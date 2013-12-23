'''
Created on Dec 14, 2013

@author: rakesh
'''
from Driver import Driver
import numpy as np


if __name__ == '__main__':

#    driver1 = Driver(2, 1000, 3, 2, np.arange(1.0, 3.5, 0.5), [5.0])
    
    driver1 = Driver(2, 1000, 3, 2, [1.0], [50.0])
    driver1.run_simulation()
    driver1.graph_process_times_with_changing_arrival_rate()
    