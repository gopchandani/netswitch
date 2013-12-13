'''
Created on Nov 19, 2013

@author: rakesh
'''

import os
import glob

from pyparsing import *
from pylab import *

pp_floatNumber                  =   Regex(r'[-+]?\d+(\.\d*)?([eE][-+]\d+)?')

pp_filekeyword                  =   Literal('Results_Experiment_').setResultsName('pp_filekeyword')
pp_fileindex                    =   Word(nums).setResultsName('pp_fileindex')
pp_basename_parts               =   (pp_filekeyword + pp_fileindex).setResultsName('pp_basename_parts')

pp_arrival_rate_keyword                     =   Literal('ArrivalRate = ').setResultsName('pp_arrival_rate_keyword')
pp_cost_per_level_keyword                   =   Literal('CostPerLevel = ').setResultsName('pp_cost_per_level_keyword')
pp_distribution_intercept_keyword           =   Literal('DistributionIntercept = ').setResultsName('pp_distribution_intercept_keyword')
pp_distribution_slope_keyword               =   Literal('DistributionSlope = ').setResultsName('pp_distribution_slope_keyword')
pp_max_queue_size_keyword                   =   Literal('MaxQueueSize = ').setResultsName('pp_max_queue_size_keyword')

pp_parameter_keyword            =   Or([pp_arrival_rate_keyword, pp_cost_per_level_keyword, pp_distribution_intercept_keyword, pp_distribution_slope_keyword, pp_max_queue_size_keyword]).setResultsName('pp_parameter_keyword')
pp_parameter_value              =   pp_floatNumber.setResultsName('pp_parameter_value')  

pp_parameter_line               =   (pp_parameter_keyword + pp_parameter_value).setResultsName('pp_parameter_line')


pp_avgqueuesize                 =   Literal('Performance variable :  AvgQueueSize').setResultsName('pp_avgqueuesize')
pp_variable_mean_keyword        =   Literal('Mean                 :  ').setResultsName('pp_variable_mean_keyword')
pp_variable_mean                =   (pp_variable_mean_keyword + pp_parameter_value).setResultsName('pp_variable_mean')
pp_variable_variance_keyword    =   Literal('Variance             :  ').setResultsName('pp_variable_variance_keyword')
pp_variable_variance            =   (pp_variable_variance_keyword + pp_parameter_value).setResultsName('pp_variable_variance')



def pickup_solution_data(solution_name):

    data = {}
    
    arrival_rate_d = {}
    cost_per_level_d = {}
    distribution_intercept_d = {}
    distribution_slope_d = {}
    max_queue_size_d = {}
    avg_queue_size_mean_d = {}
    avg_queue_size_variance_d = {}
    avg_queue_size_stdev_d = {}
    avg_time_to_process_d = {}
    
    solution_glob_input = '../input/' + solution_name + '/*.txt'
    inputfilepaths = glob.glob(solution_glob_input)    
    
    for inputfile in inputfilepaths:
        
        basename = os.path.basename(inputfile)
        filenametokens = pp_basename_parts.parseString(basename)
        
        index = int(filenametokens.pp_fileindex)
        arrival_rate = None
        cost_per_level = None
        distribution_intercept = None
        distribution_slope = None
        max_queue_size = None
        avg_queue_size_mean = None
        avg_queue_size_variance = None
        
        f = open(inputfile, 'r')
        for line in f:
            try:
                #First parse the parameters
                
                parameter_tokens = pp_parameter_line.parseString(line)       
                
                if parameter_tokens.pp_arrival_rate_keyword != '':
                    arrival_rate = parameter_tokens.pp_parameter_value

                if parameter_tokens.pp_cost_per_level_keyword != '':
                    cost_per_level = parameter_tokens.pp_parameter_value

                if parameter_tokens.pp_distribution_intercept_keyword != '':
                    distribution_intercept = parameter_tokens.pp_parameter_value

                if parameter_tokens.pp_distribution_slope_keyword != '':
                    distribution_slope = parameter_tokens.pp_parameter_value

                if parameter_tokens.pp_max_queue_size_keyword != '':
                    max_queue_size = parameter_tokens.pp_parameter_value                
                
                
            except:
                pass

        f = open(inputfile, 'r')
        lines = f.readlines()
        for i in range(len(lines)):
            try:
                avgqueuesize_tokens = pp_avgqueuesize.parseString(lines[i])
                
                pp_variable_mean_tokens = pp_variable_mean.parseString(lines[i+1])
                avg_queue_size_mean = pp_variable_mean_tokens.pp_parameter_value
                pp_variable_variance_tokens = pp_variable_variance.parseString(lines[i+2])
                avg_queue_size_variance = pp_variable_variance_tokens.pp_parameter_value             

            except:
                pass
        
        #print index, arrival_rate, cost_per_level, distribution_intercept, distribution_slope, max_queue_size, avg_queue_size_mean, avg_queue_size_variance
        arrival_rate_d[index]               = float(arrival_rate)
        cost_per_level_d[index]             = float(cost_per_level)
        distribution_intercept_d[index]     = float(distribution_intercept)
        
        if distribution_slope != None:
            distribution_slope_d[index]         = float(distribution_slope)
        
        max_queue_size_d[index]             = float(max_queue_size)
        avg_queue_size_mean_d[index]        = float(avg_queue_size_mean)
        avg_queue_size_variance_d[index]    = float(avg_queue_size_variance)
        avg_queue_size_stdev_d[index]       = sqrt(float(avg_queue_size_variance))
        avg_time_to_process_d[index]        = avg_queue_size_mean_d[index] / arrival_rate_d[index]
    
    data['arrival_rate_d'] = arrival_rate_d
    data['cost_per_level_d'] = cost_per_level_d
    data['distribution_intercept_d'] = distribution_intercept_d
    data['distribution_slope_d'] = distribution_slope_d
    data['max_queue_size_d'] = max_queue_size_d
    data['avg_queue_size_mean_d'] = avg_queue_size_mean_d
    data['avg_queue_size_variance_d'] = avg_queue_size_variance_d
    data['avg_queue_size_stdev_d'] = avg_queue_size_stdev_d
    
    data['avg_time_to_process_d'] = avg_time_to_process_d
    
    return data

def generate_plot(xlist, ylist, xlab, ylab, solution_name):
    
    x = array(xlist)
    y = array(ylist)
    
    plt.plot(x, y)
    
    xlabel(xlab)
    ylabel(ylab)
    
    
    outputpath = '../output/' + solution_name + '.pdf'
    plt.savefig(outputpath)
    plt.show()

    
def process_solution(solution_name):
    
    data = pickup_solution_data(solution_name)
    
#    generate_plot(data['avg_time_to_process_d'].values(), data['cost_per_level_d'].values(), \
#                  'Average Time to Process',  'Cost Per Level', solution_name)        

    generate_plot(\
                  data['cost_per_level_d'].values(), \
                  data['avg_time_to_process_d'].values(), \
                  'Cost Per Level', \
                  'Average Time to Process',  \
                  solution_name)        


    
if __name__ == '__main__':
    
    process_solution('incident_isss_positive_slope')
    process_solution('incident_isss_zero_slope')
    process_solution('incident_isss_negative_slope')

