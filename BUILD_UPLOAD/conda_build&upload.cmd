cd C:\Users\ecfne\Desktop

conda build purge
conda skeleton pypi pytictoc
conda build --python 3.7 pytictoc
conda convert -f --platform all C:\Anaconda3\conda-bld\win-64\pytictoc-1.1.0-py37_0.tar.bz2 -o C:\Anaconda3\conda-bld\

anaconda upload C:\Anaconda3\conda-bld\win-64\pytictoc-1.1.0-py36_0.tar.bz2
anaconda upload C:\Anaconda3\conda-bld\win-32\pytictoc-1.1.0-py36_0.tar.bz2
anaconda upload C:\Anaconda3\conda-bld\osx-64\pytictoc-1.1.0-py36_0.tar.bz2
anaconda upload C:\Anaconda3\conda-bld\linux-64\pytictoc-1.1.0-py36_0.tar.bz2
anaconda upload C:\Anaconda3\conda-bld\linux-32\pytictoc-1.1.0-py36_0.tar.bz2