# `get_int()` Function

We'll start by creating a generic but extremely useful function called
get_int(). It will accept arguments for a minimum and maximum value and
"guarantee" to the caller that the number returned is an `int` between these two
values.

The tricky part is that this input comes not from a random number generator or
some other computer function that is reliable and sane. But instead it comes from
stupid, unreliable, unpredictable and smelly humans!!

Yeah, this is just input validation. However, in the past we gave users just one
try to get it right and otherwise we returned None or just exited the program.
This time, users get to keep trying until they get it right.

In the code file provided, change the code block for `get_int()` as follows:

 - Repeat the following until you can return a valid number
   + Ask the user for input using the prompt.
   + Try to convert that input into an int
     * if this fails print "NOT A NUMBER" and let the user try again
   + See if the user input is within the specified min/max range
     * if not, print "OUT OF RANGE" and let the user try again
   + Return the number
