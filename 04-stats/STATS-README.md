# Basic Statistics

Loops can also be used to "accumulate" values over time. The classic adding
machine is often emulated in programs to "exercise" this capability. You keep on
entering numbers and it keeps a running sum until you enter a special value and
it exits.

This exercise is a more robust twist on that exercise. Instead of JUST
calculating a sum, we'll calculate all kinds of statistics, like a count of
number, the highest number entered, the lowest, and the average.

Yes!! Statistics! My FAVORITE!!!

The user experience will be simple. You'll ask for "NUM: " repeatedly until the
user presses JUST enter (or enters anything that can't be converted into a
float). Then you'll print out the count, sum, max, min and average of the
numbers entered. Simple!

Actually it really is. The logic is basically as follows:

  - initialize your "accumulator" and "tracker" variables to keep track of the
    count, maximum, minimum and total
    + be sure to initialize everything except for the counter to  0.0 (not just
      0) since these are floats, not ints
    + be careful not to stomp on the `max()`, `min()` and `sum()` built-in
      functions...i.e., don't use those as variable names)
  - do the following "forever" (because you'll break out of the loop manually)
    + ask the user for a number and convert it to a float
      - if that fails, then exit the loop
    + add one to the count of numbers
    + add the number to the running total
    + if the number is higher than the maximum, set it as the new maximum
    + if the number is lower than the minimum, set it as the new minimum
  - when the loop is exited, print out the calculated values

The final output should be in the form:
```
COUNT: ___
TOTAL: ___
AVERAGE: ___
MINIMUM: ___
MAXIMUM: ___
```
The average is simply the total divided by the count. Don't worry about rounding.

One special case is if the user enters no numbers (i.e., the count is 0), then
just print `NO NUMBERS ENTERED` instead of the stats above.

  > HELPFUL HINT: the logic to find the minimum value is easy, BUT, it's tricky
  > because you have to "prime the pump." You need to start your minimum
  > "tracker" at an arbitrarily high value. It can be whatever, but something
  > like `1E100` is 1 followed by 100 0's, which is, you know, kinda big.

An example run:
```
NUM: 1.5
NUM: 2.5
NUM: 5
NUM: 3
NUM:
COUNT: 4
TOTAL: 12.0
AVERAGE: 3.0
MINIMUM: 1.5
MAXIMUM: 5.0
```
