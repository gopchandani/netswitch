'''
Created on Dec 14, 2013

@author: rakesh
'''
from Driver import Driver


if __name__ == '__main__':
    
    driver = Driver(10, 1000)
    
    driver.run_simulation()
    
    driver.display_graph_of_wait_times_with_changing_arrival_rate()
    