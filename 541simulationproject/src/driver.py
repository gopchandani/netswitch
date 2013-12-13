'''
Created on Dec 10, 2013

@author: rakesh
'''

import logging
import simpy
from Update import Update


if __name__ == '__main__':
    
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    
    env = simpy.Environment()
    Update = Update(env, 1.0, 100, 10.0)
    env.run(until=10000)
    