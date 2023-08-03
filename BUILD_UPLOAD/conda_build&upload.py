# -*- coding: utf-8 -*-

"""
Build and upload conda package for pytictoc from PyPi package for various versions
of Python and OS

Author: Eric Fields
Version Date: 2 August 2023
"""

import os
from os.path import join

def main():
    
    #Directories
    conda_build_dir = r'C:\Users\fieldsec\AppData\Local\anaconda3\conda-bld'
    os.chdir(r'C:\Users\fieldsec\OneDrive - Westminster College\Desktop')
    
    #Operating systems and versions to support
    pttver = '1.5.3'
    op_sys = ['linux-32',
              'linux-64', 
              'linux-aarch64', 
              'linux-armv6l', 
              'linux-armv7l',
              'linux-ppc64', 
              'linux-ppc64le',
              'linux-s390x',
              'osx-64',
              'osx-arm64',
              'win-32',
              'win-64',
              'win-arm64']
    versions = ['2.7', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '3.10', '3.11']
    
    #Initial build
    os.system('conda-build purge-all')
    os.system('conda skeleton pypi pytictoc')
    os.system('conda-build pytictoc')
    
    #Create build for different Python versions
    for pyver in versions:
        os.system('conda-build --python %s pytictoc' % pyver)
    
    #Create builds for different OS
    for pyver in (x.replace('.', '') for x in versions):
        tar_file = join(conda_build_dir, 'win-64', 'pytictoc-%s-py%s_0.tar.bz2' % (pttver, pyver))
        os.system(('conda convert -f --platform all %s -o %s' 
                   % (tar_file, conda_build_dir)) + os.sep)
    
    #Upload to Anaconda
    for pyver in (x.replace('.', '') for x in versions):
        for ossys in op_sys:
            upload_file = join(conda_build_dir, ossys, 'pytictoc-%s-py%s_0.tar.bz2' % (pttver, pyver))
            os.system('anaconda upload %s' % upload_file)
    
    os.system('anaconda logout')
    
if __name__ == '__main__':
    main()
