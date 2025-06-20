# GUESSING GAME

Let's make a simple "guess the number I'm thinking of" game, but let the
user try a specific number of times.

The goal here is to implement the `game()` function. This function accepts two
arguments. The first, `max_guess`, is an int that provides the upper bound of the
guesses (i.e., guess a number between 1 and max_guess). The other,
`num_guesses`, is how many guesses the user is allowed. The function should
return True if the user guesses correctly. But if the user exceeds the number of
allowed guesses, the function should return False. Detailed requirements for the
operation of the `game()` function are as follows:

 -  Generate and remember a random int between 1 and `max_guess`
 -  Use a counter-controlled loop to repeat the following `num_guesses` times
    + Use the `get_int()` function to ask the user to "Enter a number from 1 to
      `max_guess`: "
    + Use conditional logic to tell the user "TOO HIGH" or "TOO LOW" or "YES,
      THAT'S IT"
      * If the user guesses right, then you should return True, thus exiting
        both the loop and the function "early"
      * If the guess is wrong, there should be nothing to do other than print
        the message and continue looping. And since this is the end of the loop,
        the `continue` statement isn't really needed either, is it?
    + ( *Don't forget to increment your counter somewhere so you don't end up in an
      infinite loop.* )
 -  If the loop ends, then this means the user didn't guess the number. Print
    "SORRY, IT WAS `blah`" where `blah` is the random number you generated at
    the start of the loop. Then return False.
