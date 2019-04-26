pytictoc contains a class TicToc which replicates the functionality of MATLAB's tic and toc for easily timing sections of code. Under the hood, pytictoc uses the default_timer function from Python's timeit module.

=============
INSTALLATION
=============

pytictoc can be installed and updated via conda or pip.

**pip** ::
 
  pip install pytictoc
  pip install pytictoc --upgrade

**conda** ::

  conda install pytictoc -c ecf
  conda update pytictoc -c ecf


=============
USAGE
============= 

Basic usage: ::

  >> from pytictoc import TicToc
  >> t = TicToc() #create instance of class

  >> t.tic() #Start timer
  >> t.toc() #Time elapsed since t.tic()
  Elapsed time is 2.612231 seconds.

A string passed to the toc method changes the printed message. This can be useful to differentiate timing of different sections in the same script. ::

  >> t.toc('Section 1 took')
  Section 1 took 16.494467 seconds.

An optional keyword argument restarts the timer (equivalent to t.tic()) after reporting the time elapsed. ::

  >> t.toc(restart=True)
  Elapsed time is 36.986837 seconds.
  >>t.toc()
  Elapsed time is 2.393425 seconds.

If you want to return the time elapsed to a variable rather than printing it, use the tocvalue method. ::

  >>spam = t.tocvalue()
  >>spam
  20.156261717544602

The TicToc class can be used within a context manager as an alternative way to time a section of code. The time taken to run the code inside the with statement will be reported on exit. ::
 
  >>with TicToc():
  >>    spam = [x+1 for x in range(10000)]
  Elapsed time is 0.002343 seconds.

------------------------------------
Determining and setting the timer
------------------------------------

pytictoc uses timeit.default_timer to time code. On Python 3.3 and later, this is an alias for time.perf_counter. On earlier versions of Python it is an alias for the most precise timer for a given system. 

To see which function is being used: ::

  >>import pytictoc
  >>pytictoc.default_timer
  <function time.perf_counter>

You can change the timer by simple assignment. ::
  
  >>import time
  >>pytictoc.default_timer = time.clock
  >>pytictoc.default_timer
  <function time.clock>
