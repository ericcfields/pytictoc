# -*- coding: utf-8 -*-

"""
Build and upload conda package for pytictoc from PyPi package for various versions
of Python and OS

Author: Eric Fields
Version Date: 23 April 2021
"""

import os
from os.path import join

def main():
    
    #Directories
    conda_build_dir = r'C:\Anaconda3\envs\py38\conda-bld'
    os.chdir(r'C:\Users\ecfne\Desktop')
    
    #Operating systems and versions to support
    pttver = '1.5.2'
    op_sys = ['win-64', 'win-32', 'osx-64', 'linux-64', 'linux-32']
    versions = ['2.7', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9']
    
    #Initial build
    os.system('conda-build purge-all')
    os.system('conda skeleton pypi')
    os.system('conda-build pytictoc')
    
    #Create build for different Python versions
    for pyver in versions:
        os.system('conda-build --python %s pytictoc' % pyver)
    
    #Create builds for different OS and then upload to Anaconda
    for pyver in (x.replace('.', '') for x in versions):
        tar_file = join(conda_build_dir, 'win-64', 'pytictoc-%s-py%s_0.tar.bz2' % (pttver, pyver))
        os.system(('conda convert -f --platform all %s -o %s' 
                   % (tar_file, conda_build_dir)) + os.sep)
        for ossys in op_sys:
            upload_file = join(conda_build_dir, ossys, 'pytictoc-%s-py%s_0.tar.bz2' % (pttver, pyver))
            os.system('anaconda upload %s' % upload_file)
    
    os.system('anaconda logout')
    
if __name__ == '__main__':
    main()
