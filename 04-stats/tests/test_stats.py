from io import StringIO
import unittest
import sys
from pathlib import Path
from unittest.mock import patch


script_name = '../stats.py'
file = (Path(__file__).parent / script_name).resolve()
script_text = open(file).read()

def _format_stats(strs):
    nums = [float(n) for n in strs[:-1]] # assume all but the last is a valid float str
    if nums:
        return (f"COUNT: {len(nums)}",
                f"TOTAL: {sum(nums)}",
                f"AVERAGE: {sum(nums) / len(nums)}",
                f"MINIMUM: {min(nums)}",
                f"MAXIMUM: {max(nums)}")
    else:
        return ("NO NUMBERS ENTERED", )

class TestStats(unittest.TestCase):

    def _stats(self, inputs, extra_message=""):
        with patch('builtins.input') as mock_input:
            exp_out = _format_stats(inputs)
            mock_input.side_effect = inputs
            captured_output = StringIO()
            sys.stdout = captured_output
            try:
                exec(script_text)
            except SystemExit:
                pass
            sys.stdout = sys.__stdout__
            act_out = captured_output.getvalue().strip().splitlines()
            message = f'''
When I ran the program with the following inputs:

{'\n'.join(inputs)}
I expected to see:

{'\n'.join(exp_out)}

But I saw:

{'\n'.join(act_out)}
{extra_message}
'''
        for i in range(len(exp_out)):
            if i < len(act_out):
                exp = exp_out[i].lower()
                act = act_out[i].lower()
                self.assertIn(exp, act, message)

    def test_stats_4_and_enter(self):
        self._stats(['1.5','2.5','5','3',''])

    def test_stats_1_and_bogus(self):
        self._stats(['1.5','2.5','5','3','cornholio'])

    def test_stats_mixed_pos_and_neg(self):
        self._stats(['1.5','-1.5','5','4','8','10.333',''])

    def test_stats_only_zero(self):
        self._stats(['0',''], "\nDid you initialize your tracker values to 0.0 instead of just 0 to make sure they are floats?")

    def test_stats_sums_to_zero(self):
        self._stats(['1.5','-1.5','5','-5',''])

    def test_stats_just_enter(self):
        self._stats([''])



if __name__ == '__main__':
    unittest.main()
