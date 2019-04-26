# -*- coding: utf-8 -*-
"""
Script to test pytictoc
"""

import os
import sys

if sys.version_info.major == 3:
    from importlib import reload
    
os.chdir(r'C:\Users\efield02\Documents\Eric (Local)\Coding\Python\pytictoc')

try:
    reload(pytictoc)
except (NameError, ImportError):
    import pytictoc
    
def waste_time(num_reps=1000000):
    for i in range(num_reps):
        spam = i+1
        eggs = spam**2
        pancakes = eggs % 3
    
def main():

    print('\npytictoc file:')
    print(pytictoc.__file__ + '\n')
    
    t = pytictoc.TicToc()
    
    t.tic()
    waste_time()
    t.toc()
    
    with pytictoc.TicToc():
        waste_time()
    
    t.toc('It has been', restart=True)
    t.toc()
    
    spam = t.tocvalue()
    print(spam)
    
    waste_time()
    
    spam = t.tocvalue(restart=True)
    print(spam)
    t.toc()
    
if __name__ == '__main__':
    main()
