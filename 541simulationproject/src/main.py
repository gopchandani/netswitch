'''
Created on Dec 14, 2013

@author: rakesh
'''
from Driver import Driver
import numpy as np


if __name__ == '__main__':


    driver3 = Driver(20, 100, 3, 2, np.arange(1.0, 5.0, 0.5), np.arange(1.0, 5.0, 0.5), [0.0, 0.33, 0.67, 1.0])
#    driver3.run_simulation()
#    driver3.graph_process_times_with_changing_arrival_rate()
    
    driver3.run_2_k_study()
