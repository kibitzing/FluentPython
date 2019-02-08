#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" memtest examples

"""        
import importlib
import sys
import resource

NUM_VECTORS = 10**7

def hello(name):
    return print('Hello, {}!'.format(name))
    
module = importlib.import_module('os')
fmt = 'Selected os type: {.__name__}'
print(fmt.format(module, module.makedirs))

mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print('Creating {:,} os instances'.format(NUM_VECTORS))

vectors = [module.makedirs for i in range(NUM_VECTORS)]

mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print('Initial RAM usage: {:14,}'.format(mem_init))
print('  FInal RAM usage: {:14,}'.format(mem_final))