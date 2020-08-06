# -*- coding: utf-8 -*-
#Written in Python 3.6

#AUTHOR: Eric Fields
#VERSION DATE: 6 August 2020

"""
Build and upload conda package for pytictoc from PyPi package for various versions
of Python and OS
"""

#1. cd C:\Users\ecfne\Desktop
#2. conda build purge
#3. conda skeleton pypi pytictoc
#4. conda build pytictoc
#5. update paths below if necessary

import os

def main():
    
    os.chdir(r'C:\Users\ecfne\Desktop')
    
    #Operating systems and versions to support
    pttver = '1.5.1'
    op_sys = ['win-64', 'win-32', 'osx-64', 'linux-64', 'linux-32']
    versions = ['2.7', '3.4', '3.5', '3.6', '3.7', '3.8']
    
    for pyver in versions:
        os.system('conda build --python %s pytictoc' % pyver)
    
    for pyver in (x.replace('.', '') for x in versions):
        os.system(('conda convert -f --platform all C:\Anaconda3\conda-bld\win-64\pytictoc-%s-py%s_0.tar.bz2 -o C:\Anaconda3\conda-bld' % (pttver, pyver))
                    + os.sep)
        for ossys in op_sys:
            os.system('anaconda upload C:\Anaconda3\conda-bld\%s\pytictoc-%s-py%s_0.tar.bz2' % (ossys, pttver, pyver))
    
    os.system('anaconda logout')
    
if __name__ == '__main__':
    main()