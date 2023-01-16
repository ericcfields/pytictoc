import contextlib
import re
import time
import unittest
from abc import ABCMeta
from io import StringIO

from .. import pytictoc as ptt


class BaseTicTocTest(unittest.TestCase, metaclass=ABCMeta):

    def setUp(self):
        self.mock_time = 0
        self.stream = StringIO()
        self.tt = ptt.TicToc(default_msg="Time:", stream=self.stream, timer=lambda: self.mock_time)

    def output(self):
        return self.stream.getvalue()

    def time_passed(self):
        return re.findall(r'([-\d\.,]+) seconds.$', self.output(), re.MULTILINE)

    def err_msg(self):
        raw_output = self.output().splitlines() or ["<null>"]
        return "Last output: %s" % raw_output[-1]

    def _run_tictoc(self, start_time, end_time, work_function=None, **toc_args):
        self.mock_time = start_time
        self.tt.tic()
        if work_function:
            work_function()
        self.mock_time = end_time
        self.tt.toc(**toc_args)

    def tictoc(self, start_time=0, end_time=0, **toc_args):
        self._run_tictoc(start_time, end_time, **toc_args)
        self.assertTime(start_time, self.tt.start)
        self.assertTime(end_time, self.tt.end)
        time_passed = self.time_passed()
        self.assertGreater(len(time_passed), 0, self.err_msg())
        self.assertTime(end_time - start_time, float(time_passed[-1]))
        self.assertTime(end_time - start_time, self.tt.tocvalue())

    def assertTime(self, expected, actual, *args, **kwargs):
        # Measure equality to 6 decimal places to avoid float precision errors
        self.assertAlmostEqual(expected, actual, 6, self.err_msg(), *args, **kwargs)

    def test_increment(self):
        self.tictoc(0, 1)
        self.tictoc(0, 2)
        self.tictoc(5, 9)
        self.tictoc(-9, 20)

    def test_no_time_passed(self):
        self.tictoc(0, 0)
        self.tictoc(1, 1)
        self.tictoc(-5, -5)

    def test_decrement(self):
        self.tictoc(1, 0)
        self.tictoc(5, -5)
        self.tictoc(-100, -300)

    def test_decimal(self):
        self.tictoc(0.3, 3.6)
        self.tictoc(0.3, -3.6)
        self.tictoc(0.34, 0)
        self.tictoc(0, -0.25)
        self.tictoc(-7.9, -20)
        self.tictoc(4, 25.89)

    def test_default_msg(self):
        self.tt = ptt.TicToc(stream=self.stream, timer=lambda: self.mock_time)
        self.tictoc(4, 6)
        self.assertIn("Elapsed time is 2.0", self.output())

    def test_default_stream_is_stdout(self):
        with contextlib.redirect_stdout(self.stream):
            self.tt = ptt.TicToc(default_msg="Time:", timer=lambda: self.mock_time)
            self.tictoc(-4, 8.2)
            self.tictoc(8, 16)

    def test_default_invocation_works(self):
        with contextlib.redirect_stdout(self.stream):
            self.tt = ptt.TicToc()

            # I suggest keeping a negative interval to confirm the actual time is used
            self._run_tictoc(0, -1, lambda: time.sleep(0.01))

            # NB: Prior to Python 3.5 the sleep could end early. Will still work with zero.
            self.assertGreaterEqual(float(self.time_passed()[-1]), 0)


class TicTocTest(BaseTicTocTest):
    def test_msg(self):
        self.tictoc(1, 6, msg="Tic Toc")
        self.assertIn("Tic Toc 5.0", self.output())

    def test_msg_in_stdout(self):
        with contextlib.redirect_stdout(self.stream):
            self.tt = ptt.TicToc(default_msg="Time:", timer=lambda: self.mock_time)
            self.tictoc(1, -7, msg="Tic Toc")
            self.assertIn("Tic Toc -8.0", self.output())

    def test_restart(self):
        self._run_tictoc(4, 6, restart=True)
        self.assertTime(6, self.tt.start)


class TicTocTestWithContextManager(BaseTicTocTest):
    def _run_tictoc(self, start_time, end_time, **toc_args):
        if toc_args:
            raise unittest.SkipTest("Toc arguments aren't supported with context managers")

        self.mock_time = start_time
        with self.tt:
            self.mock_time = end_time

    def test_default_invocation_works(self):
        with contextlib.redirect_stdout(self.stream):
            self.tt = ptt.TicToc()
            with self.tt:
                time.sleep(0.01)
            # NB: Prior to Python 3.5 the sleep could end early. Will still work with zero.
            self.assertGreaterEqual(float(self.time_passed()[-1]), 0)


del BaseTicTocTest  # Don't run the tests in the abstract class.

if __name__ == '__main__':
    unittest.main()
