from io import StringIO
import unittest
import sys
from pathlib import Path
from unittest.mock import patch

script_name = '../count_positive.py'
file = (Path(__file__).parent / script_name).resolve()
script_text = open(file).read()

class TestCountPositive(unittest.TestCase):

    def _run_count_positive(self, inputs, expected_output_lines):
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = inputs
            captured_output = StringIO()
            sys.stdout = captured_output
            try:
                exec(script_text)
            except SystemExit:
                pass
            sys.stdout = sys.__stdout__
            actual_output = captured_output.getvalue().strip().splitlines()

            input_text = '\n'.join(inputs)
            expected_text = '\n'.join(expected_output_lines)
            actual_text = '\n'.join(actual_output)

            message = (
                "I simulated the following inputs:\n"
                f"{input_text}\n\n"
                "I expected this output:\n"
                f"{expected_text}\n\n"
                "But got this:\n"
                f"{actual_text}"
            )

            for i in range(len(expected_output_lines)):
                if i < len(actual_output):
                    self.assertIn(expected_output_lines[i].lower(), actual_output[i].lower(), message)

    def test_no_positives(self):
        self._run_count_positive(['0'], ['You entered 0 positive number(s).'])

    def test_single_positive(self):
        self._run_count_positive(['1', '0'], ['You entered 1 positive number(s).'])

    def test_negative_then_zero(self):
        self._run_count_positive(['-5', '0'], ['You entered 0 positive number(s).'])

    def test_mixed_positive_negative_zero(self):
        self._run_count_positive(['-1', '2', '-3', '4', '0'], ['You entered 2 positive number(s).'])

    def test_many_positives(self):
        self._run_count_positive(['1', '1', '1', '1', '0'], ['You entered 4 positive number(s).'])

if __name__ == '__main__':
    unittest.main()
