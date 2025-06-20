from io import StringIO
import unittest
import sys
from pathlib import Path
from unittest.mock import patch


script_name = '../blastoff.py'
file = (Path(__file__).parent / script_name).resolve()
script_text = open(file).read()

class TestBlastoff(unittest.TestCase):

    def test_blastoff_sleep_called_with_1(self):
        with patch('time.sleep') as mock_sleep:
            with patch('random.randint') as mock_randint:
                mock_randint.side_effect = [100,1]
                try:
                    exec(script_text)
                except SystemExit:
                    pass
                try:
                    mock_sleep.assert_called_once_with(1)
                except AssertionError:
                    self.fail("\nIt doesn't appear you are calling sleep with an argument of 1.")

    def test_blastoff_random_called_with_1_and_100(self):
        with patch('time.sleep') as mock_sleep:
            with patch('random.randint') as mock_randint:
                mock_randint.side_effect = [1]
                try:
                    exec(script_text)
                except SystemExit:
                    pass
                try:
                    mock_randint.assert_called_once_with(1,100)
                except AssertionError:
                    self.fail("It doesn't appear you are calling randint with 1 and 100 as the arguments.")

    def _blastoff(self, rand_vals, exp_out):
        with patch('time.sleep') as mock_sleep:
            with patch('random.randint') as mock_randint:
                mock_randint.side_effect = rand_vals
                captured_output = StringIO()
                sys.stdout = captured_output
                try:
                    exec(script_text)
                except SystemExit:
                    pass
                sys.stdout = sys.__stdout__
                act_out = captured_output.getvalue().strip().splitlines()
                message = f'''
When the random number generator generated the following numbers: {rand_vals}
I expected to see:
{'\n'.join(exp_out)}
But I saw:
{'\n'.join(act_out)}
'''
            for i in range(len(exp_out)):
                if i < len(act_out):
                    exp = exp_out[i].lower()
                    act = act_out[i].lower()
                    self.assertIn(exp, act, message)

    def test_blastoff_success(self):
        self._blastoff(
            [100,90,80,70,60,50,40,30,20,11],
            ['10','9','8','7','6','5','4','3','2','1','BLASTOFF!'])

    def test_blastoff_last_second_hold(self):
        self._blastoff(
            [100,90,80,70,60,50,40,30,20,2],
            ['10','9','8','7','6','5','4','3','2','1','HOLD...HOLD...HOLD'])

    def test_blastoff_early_hold(self):
        self._blastoff(
            [100,90,4],
            ['10','9','8','HOLD...HOLD...HOLD'])

    def test_blastoff_immediate_rud(self):
        self._blastoff(
            [1],
            ['10','HOUSTON, WE HAVE A PROBLEM'])

    def test_blastoff_range_violation_lbound(self):
        self._blastoff(
            [13,12,11,5],
            ['10','9','8','7','RANGE VIOLATION...COUNTDOWN ABORTED'])

    def test_blastoff_range_violation_ubound(self):
        self._blastoff(
            [14,13,12,11,7],
            ['10','9','8','7','6','RANGE VIOLATION...COUNTDOWN ABORTED'])

    def test_blastoff_valve_leak_lbound(self):
        self._blastoff(
            [15,14,13,12,11,8],
            ['10','9','8','7','6','5','VALVE LEAK...COUNTDOWN ABORTED'])

    def test_blastoff_valve_leak_ubound(self):
        self._blastoff(
            [15,15,14,13,12,11,10],
            ['10','9','8','7','6','5','4','VALVE LEAK...COUNTDOWN ABORTED'])



if __name__ == '__main__':
    unittest.main()
