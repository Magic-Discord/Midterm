import sys
import os
from io import StringIO
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from guess import game


class TestGuess(unittest.TestCase):

    def setUp(self):
        # Horrid hack needed to determine which way the student is importing and
        # using randint.
        #
        #       import random
        #       from random import randint (module level)
        #       from random import randint (function level)
        #
        # Gotta love Python...
        #
        with patch("builtins.input") as mock_input:
            try:
                with patch("guess.randint") as mock_randint:
                    mock_randint.side_effect = [10]
                    mock_input.side_effect = ["10"]
                    game(15, 1)
                    if mock_randint.call_count > 0:
                        self.randint_src = "guess.randint"
                    else:
                        self.randint_src = "random.randint"
            except:
                self.randint_src = "random.randint"

    def test_game_uses_max_guess_in_prompt(self):
        with patch("builtins.input") as mock_input:
            with patch(self.randint_src) as mock_randint:
                mock_randint.side_effect = [10]
                mock_input.side_effect = ["10"]
                game(42, 1)
                args, _ = mock_input.call_args
                actual = " ".join(args)
                self.assertIn(
                    "42",
                    actual,
                    "\nI expected the input prompt to contain the value of the max_guess argument.",
                )

    def test_game_calls_random_with_correct_args(self):
        with patch("builtins.input") as mock_input:
            with patch(self.randint_src) as mock_randint:
                mock_randint.side_effect = [10]
                mock_input.side_effect = ["10"]
                game(15, 1)
                try:
                    mock_randint.assert_called_once_with(1, 15)
                except:
                    self.fail(
                        "\nI expected randint to be called with a range from 1 to max_guess."
                    )

    def _game(self, max_guess, num_guesses, secret_number, inputs, exp_out, exp_val):
        with patch("builtins.input") as mock_input:
            with patch(self.randint_src) as mock_randint:
                mock_randint.side_effect = [secret_number]
                mock_input.side_effect = [inputs]
                mock_input.side_effect = inputs
                captured_output = StringIO()
                sys.stdout = captured_output
                act_val = game(max_guess, num_guesses)
                sys.stdout = sys.__stdout__
                act_out = captured_output.getvalue().strip().splitlines()
                message = f'''
I called game({max_guess}, {num_guesses}).
The secret number was: {secret_number}
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

    def test_game_first_try(self):
        self._game(10, 3, 5, ["5"], ["YES, THAT'S IT"], True)

    def test_game_third_try_of_three(self):
        self._game(
            20,
            3,
            10,
            ["5", "15", "10"],
            ["TOO LOW", "TOO HIGH", "YES, THAT'S IT"],
            True,
        )

    def test_game_fourth_try_of_five(self):
        self._game(
            30,
            5,
            25,
            ["10", "10", "30", "25"],
            ["TOO LOW", "TOO LOW", "TOO HIGH", "YES, THAT'S IT"],
            True,
        )

    def test_game_fail_one_try(self):
        self._game(100, 1, 50, ["100"], ["TOO HIGH", "SORRY, IT WAS 50"], False)

    def test_game_fail_four_try(self):
        self._game(
            13,
            4,
            7,
            ["13", "1", "10", "4"],
            ["TOO HIGH", "TOO LOW", "TOO HIGH", "TOO LOW", "SORRY, IT WAS 7"],
            False,
        )


if __name__ == "__main__":
    unittest.main()
