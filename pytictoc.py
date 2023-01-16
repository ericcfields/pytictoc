# -*- coding: utf-8 -*-

"""
Module with class TicToc to replicate the functionality of MATLAB's tic and toc.

Documentation: https://pypi.python.org/pypi/pytictoc
"""

__author__       = 'Eric Fields'
__version__      = '1.5.2'
__version_date__ = '23 April 2021'

import sys
from timeit import default_timer

class TicToc(object):

    """
    Replicate the functionality of MATLAB's tic and toc.

    #Methods
    TicToc.tic()       #start or re-start the timer
    TicToc.toc()       #print elapsed time since timer start
    TicToc.tocvalue()  #return floating point value of elapsed time since timer start

    #Attributes
    TicToc.start     #Time from timeit.default_timer() when t.tic() was last called
    TicToc.end       #Time from timeit.default_timer() when t.toc() or t.tocvalue() was last called
    TicToc.elapsed   #t.end - t.start; i.e., time elapsed from t.start when t.toc() or t.tocvalue() was last called
    """

    def __init__(self, default_msg='Elapsed time is', stream=sys.stdout):
        """
        Create instance of TicToc class.

        Optional arguments:
            default_msg     - String to replace default message of 'Elapsed time is'
            stream          - Stream to write the timer message to
        """
        self.start   = float('nan')
        self.end     = float('nan')
        self.elapsed = float('nan')
        self.default_msg = default_msg
        self.stream = stream
        assert self.default_msg is not None
        assert self.stream is not None

    def tic(self):
        """Start the timer."""
        self.start = default_timer()

    def toc(self, msg=None, restart=False):
        """
        Report time elapsed since last call to tic().

        Optional arguments:
            msg     - String to replace default message initialized with the object
            restart - Boolean specifying whether to restart the timer
        """
        if msg is None:
            msg = self.default_msg

        self.end     = default_timer()
        self.elapsed = self.end - self.start
        print(self.tocmsg(msg, self.elapsed), file=self.stream)
        if restart:
            self.start = default_timer()

    def tocvalue(self, restart=False):
        """
        Return time elapsed since last call to tic().

        Optional argument:
            restart - Boolean specifying whether to restart the timer
        """
        self.end     = default_timer()
        self.elapsed = self.end - self.start
        if restart:
            self.start = default_timer()
        return self.elapsed

    def tocmsg(self, prefix_msg, elapsed):
        """
        Return full message that will be output on toc().

        Arguments:
            prefix_msg: preamble to the timer output
            elapsed: time elapsed
        """
        return '%s %f seconds.' % (prefix_msg, elapsed)

    def __enter__(self):
        """Start the timer when using TicToc in a context manager."""
        self.start = default_timer()

    def __exit__(self, *args):
        """On exit, print time elapsed since entering context manager."""
        self.end = default_timer()
        self.elapsed = self.end - self.start
        print(self.tocmsg(self.default_msg, self.elapsed), file=self.stream)
