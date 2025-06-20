from io import StringIO
import unittest
import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from get_yes_no import get_yes_no

class TestGetYesNo(unittest.TestCase):

    def test_get_yes_no_uses_prompt(self):
        with patch('builtins.input', side_effect=['yes']) as mock_input:
            prompt = "Continue? "
            result = get_yes_no(prompt)
            mock_input.assert_called()
            self.assertEqual(result, True)

    def _run_case(self, inputs, expected_output_count, expected_value):
        with patch('builtins.input', side_effect=inputs):
            captured = StringIO()
            sys.stdout = captured
            result = get_yes_no("Your response: ")
            sys.stdout = sys.__stdout__
            output_lines = captured.getvalue().strip().splitlines()

            self.assertEqual(result, expected_value)
            self.assertEqual(len([line for line in output_lines if "please enter" in line.lower()]), expected_output_count)

    def test_yes_immediate(self):
        self._run_case(['yes'], 0, True)

    def test_no_immediate(self):
        self._run_case(['no'], 0, False)

    def test_yes_after_one_invalid(self):
        self._run_case(['maybe', 'yes'], 1, True)

    def test_no_after_three_invalids(self):
        self._run_case(['uh', 'ok', 'hello', 'no'], 3, False)

if __name__ == '__main__':
    unittest.main()
