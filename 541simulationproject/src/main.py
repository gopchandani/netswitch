'''
Created on Dec 14, 2013

@author: rakesh
'''
from Driver import Driver
import numpy as np


if __name__ == '__main__':


#    driver3 = Driver(2, 100, [5], 2, np.arange(1.0, 5.0, 0.5), [5.0], [0.0, 0.1, 0.33, 0.5, 0.67, 0.9, 1.0])
    driver3 = Driver(2, 100, [5], 2, [1.0], [5.0], [0.1, 0.5])
    
    driver3.run_simulation()
    #driver3.run_2_k_study()

    driver3.graph_process_times_with_changing_arrival_rate()
    driver3.graph_process_times_with_changing_hopping_probability()