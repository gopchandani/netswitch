'''
Created on Dec 14, 2013

@author: rakesh
'''
import logging
from Driver import Driver


if __name__ == '__main__':
    
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.ERROR)
    driver = Driver(10)
#    driver.run_simulation()
#    driver.process_output()

    driver.run_simulation()
    
    