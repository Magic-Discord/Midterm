from io import StringIO
import unittest
import sys
import os
from unittest.mock import patch


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from get_int import get_int

class TestGetInt(unittest.TestCase):

    def test_get_int_uses_prompt(self):
        with patch('builtins.input') as mock_input:
            test_prompt = "Here kitty kitty"
            get_int(test_prompt, 1, 5)
            try:
                mock_input.assert_called_once_with(test_prompt)
            except:
                self.fail(f'''
get_input does not appear to use the prompt passed in to it.
Did you call input(prompt)??''')


    def _get_int(self, min_val, max_val, inputs, exp_out, exp_val):
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = inputs
            captured_output = StringIO()
            sys.stdout = captured_output
            act_val = get_int('', min_val, max_val)
            sys.stdout = sys.__stdout__
            act_out = captured_output.getvalue().strip().splitlines()
            message = f'''
I called get_int('A prompt:', {min_val}, {max_val}).
I typed in:
{'\n'.join(inputs)}
I expected to see:
{'\n'.join(exp_out)}
And to get back the value: {exp_val}
I saw:
{'\n'.join(act_out)}
and got back: {act_val}
'''
            self.assertEqual(exp_val, act_val, message)
            for i in range(len(exp_out)):
                if i < len(act_out):
                    exp = exp_out[i].lower()
                    act = act_out[i].lower()
                    self.assertIn(exp, act, message)

    def test_get_int_lower_bound_input(self):
        self._get_int(20, 30, ['20'], [], 20)

    def test_get_int_upper_bound_input(self):
        self._get_int(1, 25, ['25'], [], 25)

    def test_get_int_one_bad_input(self):
        self._get_int(1, 5, ['abc','3'], ['NOT A NUMBER'], 3)

    def test_get_int_three_bad_inputs(self):
        self._get_int(1, 5, ['abc','def','ghi','3'], ['NOT A NUMBER','NOT A NUMBER','NOT A NUMBER'], 3)

    def test_get_int_one_high_input(self):
        self._get_int(5, 15, ['25','10'], ['OUT OF RANGE'], 10)

    def test_get_int_one_low_input(self):
        self._get_int(5, 15, ['3','10'], ['OUT OF RANGE'], 10)

    def test_get_int_three_out_of_range_input(self):
        self._get_int(10, 20, ['1','25','60','15'], ['OUT OF RANGE','OUT OF RANGE','OUT OF RANGE'], 15)

if __name__ == '__main__':
    unittest.main()
